# NDJSON to PCAP Conversion Script

## Overview
This script converts NDJSON (Newline Delimited JSON) files to PCAP (Packet Capture) format. It reads an NDJSON file, extracts relevant fields, and constructs PCAP packets, which are then saved to an output PCAP file.
## Installation

```bash
git clone https://github.com/irregularchat/ndjson-to-pcap.git
```

## Usage

To use the script, you need to have Python installed. You can run the script from the command line as follows:

```bash
python ndjson-to-pcap.py <path_to_ndjson_file> <path_to_output_pcap_file>
```

### Example
```bash
python ndjson-to-pcap.py data/input.ndjson data/output.pcap
```

If you do not provide the necessary arguments, the script will display usage instructions.

## Requirements
- Python 3.x
- pcapng module

You can install the required module using pip requirements file:
    
```bash
pip install -r requirements.txt
```

## Troubleshooting
If the provided script does not work as expected, you may want to verify the NDJSON file format and ensure that all necessary fields (source IP, destination IP, timestamp, and payload) are present in each line of the NDJSON file.

### Alternative
If this script does not work for your needs, consider trying [json2pcap](https://github.com/H21lab/json2pcap) as an alternative, though some users have reported issues with it.

## Contributing
If you encounter any issues or have suggestions for improvements, please feel free to open an issue or submit a pull request.
- Fork the repository
- Clone the repository: `git clone URL of your fork`
- Navigate to the repository directory: `cd ndjson-to-pcap`
- Make your changes
- Commit your changes: `git commit -m 'Improve feature'`
- Push to the branch: `git push origin improve-feature`
