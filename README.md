# TFRecorder

> Simple tool which converts your NLP dataset to TFRecord file and uploads to Cloud Storage for GPU/TPU training

- [Korean (한국어) README](https://github.com/harrydrippin/tfrecorder/blob/master/README.ko.md)

## Key Feature

- [x] Generate TFRecord files by given CSV, TSV files and Metadata
- [x] Upload to Google Cloud Storage for convenient usage while using TPU with TensorFlow
- [ ] Do convert and upload simultaneously by using `asyncio.Queue`

## Metadata File Usage

```json
{
  "name": "<Name of the dataset. Will be used for TFRecord file name and GCS bucket name.>",
  "convert": {
    "from_path": "<Path of the dataset, by glob pattern.>",
    "file_type": "<Type of the file. Can use 'csv' or 'tsv'.>",
    "skip_header": false,
    "to_path": "<Path to store TFRecord files.>"
  },
  "columns": [
    {
      "name": "<Name of the column>",
      "feature_type": "<Type of the column value. 'str', 'bool', 'int', 'float'>"
    }
  ]
}
```

## Tool Usage

```text
$ tfr -h
usage: tfr [-h] [-m MODE] [--max-error MAX_ERROR] [-c COMPRESSION_TYPE]
           [--only-convert [ONLY_CONVERT]] [--only-upload [ONLY_UPLOAD]]
           [--batch-size BATCH_SIZE] [-g GOOGLE_APPLICATION_CREDENTIALS]
           [--max-pool-size MAX_POOL_SIZE] [--chunksize CHUNKSIZE]
           METADATA_PATH

Automatically convert CSV or TSV files to TFRecord, and upload them to Google
Cloud Storage.

positional arguments:
  METADATA_PATH         Path of JSON file which have metadata

optional arguments:
  -h, --help            show this help message and exit
  -m MODE, --mode MODE  Method to parse the file. Use tsv by default.
  --max-error MAX_ERROR
                        Max error records while parsing. Not set (-1) by
                        default.
  -c COMPRESSION_TYPE, --compression-type COMPRESSION_TYPE
                        TFRecord compression type. Use GZIP by default.
  --only-convert [ONLY_CONVERT]
                        Only convert the files, not upload to GCS
  --only-upload [ONLY_UPLOAD]
                        Only upload the files to GCS, not convert (will read
                        TFRECORD_PATH only)
  --batch-size BATCH_SIZE
                        Size of the examples one file should have. Use 1000 by
                        default.
  -g GOOGLE_APPLICATION_CREDENTIALS, --google-application-credentials GOOGLE_APPLICATION_CREDENTIALS
                        Google Application Credential JSON file path. Will use
                        environment variable as a default.
  --max-pool-size MAX_POOL_SIZE
                        Max pool size for multiprocessing. Use all cores by
                        default.
  --chunksize CHUNKSIZE
                        Chunksize for multiprocessing. Use 10 by default.
```

## Test

To test this, run the script below on your machine.

```bash
python setup.py develop
```
