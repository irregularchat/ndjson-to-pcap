# NDJSON to PCAP Conversion Script

## Overview
This script converts NDJSON (Newline Delimited JSON) files to PCAP (Packet Capture) format. It reads an NDJSON file, extracts relevant fields, and constructs PCAP packets, which are then saved to an output PCAP file.

## Usage

To use the script, you need to have Python installed. You can run the script from the command line as follows:

///bash
python ndjson-to-pcap.py <path_to_ndjson_file> [<path_to_output_pcap_file>]
///

### Example
///bash
python ndjson-to-pcap.py data/input.ndjson data/output.pcap
///

If the output PCAP file is not specified, the script will generate a PCAP file with the same name as the NDJSON file but with a `.pcap` extension. If the provided output filename does not have a `.pcap` extension, it will be appended automatically.

## Requirements
- Python 3.x
- pcapng module

You can install the required module using pip:

///bash
pip install -r requirements.txt
///

## Troubleshooting
If the provided script does not work as expected, you may want to verify the NDJSON file format and ensure that all necessary fields (source IP, destination IP, timestamp, and payload) are present in each line of the NDJSON file.

### Alternative
If this script does not work for your needs, consider trying [json2pcap](https://github.com/H21lab/json2pcap) as an alternative, though some users have reported issues with it.

## Contributing
If you encounter any issues or have suggestions for improvements, please feel free to open an issue or submit a pull request.

## License
This project is licensed under the MIT License - see the LICENSE file for details.
