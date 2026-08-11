# Colab CLI

## Dependencies

As of 2026-08-10, the Colab CLI requires Python 3.13.

## Demo

Check the version of Colab CLI:

```bash
colab version
```

```
Version: 0.6.0
```

Create a new Colab session named "demo" with GPU T4:

```bash
colab new -s demo --gpu T4
```

```
[colab] Creating session 'demo'...
[colab] Session READY.
```

Check the list of Colab sessions:

```bash
colab sessions
```

```
[demo] gpu-t4-s-kkb-ass1c0-1dhy42bius402 | Hardware: T4 | Variant: GPU
```

Execute the local script `test.py` in the `demo` session. The script prints the GPU availability and device name, and creates a file named `hello.txt` in the remote session.

```bash
colab exec -s demo -f test.py
```

```
GPU Available: True
Device Name: Tesla T4
```

Check the status of the `demo` session:

```bash
colab status -s demo
```

```
[demo] gpu-t4-s-kkb-ass1c0-1dhy42bius402 | Hardware: T4 | Variant: GPU | Status: IDLE
  Last Execution: test.py at 2026-08-10 14:23:21
```

List the remote files in the `demo` session:

```bash
colab ls -s demo
```

```
.config/
sample_data/
hello.txt
```

Download the remote file `hello.txt` from the `demo` session to the local machine:

```bash
colab download -s demo /content/hello.txt ./hello.txt
```

```
[colab] Downloaded '/content/hello.txt' to './hello.txt'
```

Stop the `demo` session:

```bash
colab stop -s demo
```

```
[colab] Stopping session 'demo'...
[colab] Session terminated.
```

## References

- https://developers.googleblog.com/introducing-the-google-colab-cli/
- https://github.com/googlecolab/google-colab-cli/
