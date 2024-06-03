# ndjson-to-pcap.py

import json
import argparse
import os
from pcapng import savefile
import pcapng

def convert_ndjson_to_pcap(ndjson_file, pcap_file):
    try:
        # Check if the input file is NDJSON
        if not ndjson_file.endswith('.ndjson'):
            raise ValueError("Input file is not an NDJSON file.")

        # Determine the output file name
        if not pcap_file:
            pcap_file = os.path.splitext(ndjson_file)[0] + '.pcap'
        elif not pcap_file.endswith('.pcap'):
            pcap_file += '.pcap'

        # Open NDJSON file
        with open(ndjson_file, 'r') as ndjson:
            # Open PCAP file for writing
            with savefile.SavefileWriter(pcap_file, linktype=1) as pcap:
                # Read each line from NDJSON file
                for line in ndjson:
                    try:
                        # Parse JSON
                        packet_data = json.loads(line)
                        
                        # Extract relevant fields (e.g., source IP, destination IP, etc.)
                        source_ip = packet_data.get('source_ip')
                        destination_ip = packet_data.get('destination_ip')
                        timestamp = packet_data.get('timestamp')
                        payload = packet_data.get('payload')
                        
                        # Ensure all necessary fields are present
                        if not all([source_ip, destination_ip, timestamp, payload]):
                            print(f"Skipping incomplete packet data: {line}")
                            continue
                        
                        # Construct PCAP packet
                        packet = pcapng.Packet(
                            timestamp=timestamp,
                            packet_data=payload.encode('utf-8'),
                            packet_len=len(payload),
                            src_ip=source_ip,
                            dst_ip=destination_ip
                        )
                        
                        # Add packet to PCAP file
                        pcap.packet(packet)
                    
                    except json.JSONDecodeError:
                        print(f"Error decoding JSON line: {line}")
                    except KeyError as e:
                        print(f"Missing key {e} in line: {line}")
                    except Exception as e:
                        print(f"Unexpected error processing line {line}: {e}")

        print(f"Conversion completed. PCAP file saved as {pcap_file}")

    except ValueError as ve:
        print(ve)
    except FileNotFoundError:
        print(f"NDJSON file {ndjson_file} not found.")
    except IOError as e:
        print(f"Error reading/writing file: {e}")

if __name__ == "__main__":
    # Argument parser for command line arguments
    parser = argparse.ArgumentParser(description="Convert NDJSON to PCAP")
    parser.add_argument("ndjson_file", nargs='?', help="Path to the NDJSON file")
    parser.add_argument("pcap_file", nargs='?', help="Path to the output PCAP file")

    args = parser.parse_args()

    if not args.ndjson_file:
        parser.print_help()
    else:
        # Convert NDJSON to PCAP
        convert_ndjson_to_pcap(args.ndjson_file, args.pcap_file)
