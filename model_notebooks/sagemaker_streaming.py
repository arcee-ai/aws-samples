import io
import json

# source: https://aws.amazon.com/blogs/machine-learning/elevating-the-generative-ai-experience-introducing-streaming-support-in-amazon-sagemaker-hosting/
# https://github.com/aws-samples/sagemaker-hosting/tree/main/GenAI-Hosting/Large-Language-Model-Hosting/LLM-Streaming/llama-2-hf-tgi


class LineIterator:
    """
    A helper class for parsing the byte stream input.

    The output of the model will be in the following format:
    ```
    b'{"outputs": [" a"]}\n'
    b'{"outputs": [" challenging"]}\n'
    b'{"outputs": [" problem"]}\n'
    ...
    ```

    While usually each PayloadPart event from the event stream will contain a byte array
    with a full json, this is not guaranteed and some of the json objects may be split across
    PayloadPart events. For example:
    ```
    {'PayloadPart': {'Bytes': b'{"outputs": '}}
    {'PayloadPart': {'Bytes': b'[" problem"]}\n'}}
    ```

    This class accounts for this by concatenating bytes written via the 'write' function
    and then exposing a method which will return lines (ending with a '\n' character) within
    the buffer via the 'scan_lines' function. It maintains the position of the last read
    position to ensure that previous bytes are not exposed again.
    """

    def __init__(self, stream):
        self.byte_iterator = iter(stream)
        self.buffer = io.BytesIO()
        self.read_pos = 0

    def __iter__(self):
        return self

    def __next__(self):
        while True:
            self.buffer.seek(self.read_pos)
            line = self.buffer.readline()
            if line and line[-1] == ord('\n'):
                self.read_pos += len(line)
                return line[:-1]
            try:
                chunk = next(self.byte_iterator)
            except StopIteration:
                if self.read_pos < self.buffer.getbuffer().nbytes:
                    continue
                raise
            if 'PayloadPart' not in chunk:
                print('Unknown event type:' + chunk)
                continue
            self.buffer.seek(0, io.SEEK_END)
            self.buffer.write(chunk['PayloadPart']['Bytes'])


# https://aws.amazon.com/blogs/machine-learning/elevating-the-generative-ai-experience-introducing-streaming-support-in-amazon-sagemaker-hosting/
# Modified to support the OpenAI messages format and display the total number of tokens

def print_event_stream(event_stream):
    start_json = b'{'
    stop_token = '</s>'

    for line in LineIterator(event_stream):
        if line != b'' and start_json in line:
            data = json.loads(line[line.find(start_json):].decode('utf-8'))
            #print(data)
            data = data['choices'][0]
            if "content" in data['delta']:
                content = data['delta']['content']
                if content != stop_token:
                    print(content, end='')
                else:
                    print(f"\n\nNumber of tokens: {data['index']}")