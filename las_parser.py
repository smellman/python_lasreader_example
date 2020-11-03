#!/usr/bin/env python3
import struct
import array
import sys
import os

def parse_header(f):
    file_signature = b"".join(list(struct.unpack('4c', f.read(1*4)))).decode('ascii')
    print(f"file_signature {file_signature}")
    (file_source_id,) = struct.unpack('H', f.read(2))
    print(f"file_source_id {file_source_id}")
    (global_encoding,) = struct.unpack('H', f.read(2)) #8
    print(f"global_encoding {global_encoding}")
    (guid_data1,) = struct.unpack('<L', f.read(4)) #12
    print(f"guid_data1 {guid_data1}")
    (guid_data2,) = struct.unpack('H', f.read(2)) #14
    print(f"guid_data2 {guid_data2}")
    (guid_data3,) = struct.unpack('H', f.read(2)) #16
    print(f"guid_data3 {guid_data3}")
    guid_data4 = struct.unpack('<8B', f.read(1*8)) #24
    print(f"guid_data4 {guid_data4}")
    (version_major, version_minor,) = struct.unpack('bb', f.read(1*2)) #26
    print(f"version {version_major} {version_minor}")
    system_identifier = b"".join(list(struct.unpack('32c', f.read(1*32)))).decode('ascii') #58
    generate_software = b"".join(list(struct.unpack('32c', f.read(1*32)))).decode('ascii') #90
    print(f"system_identifier {system_identifier}")
    print(f"generate_software {generate_software}")
    (create_day_of_year, create_year,) = struct.unpack('HH', f.read(2*2)) #94
    print(f"create year {create_year} day {create_day_of_year}")
    (header_size,) = struct.unpack('H', f.read(2)) #96
    print(f"header_size {header_size}")
    # o.pointsOffset = readAs(arraybuffer, Uint32Array, 32*3);
    (offset_to_point_data,) = struct.unpack('<L', f.read(4)) #100
    print(f"* offset_to_point_data {offset_to_point_data}")
    (number_of_variable_length_records,) = struct.unpack('<L', f.read(4)) #104
    print(f"number_of_variable_length_records {number_of_variable_length_records}")
    # o.pointsFormatId = readAs(arraybuffer, Uint8Array, 32*3+8);
    (point_data_format_id,) = struct.unpack('<B', f.read(1)) #105
    print(f"* point_data_format_id {point_data_format_id}")
    # o.pointsStructSize = readAs(arraybuffer, Uint16Array, 32*3+8+1); 105
    (point_data_record_length,) = struct.unpack('H', f.read(2)) #107
    print(f"* point_data_record_length {point_data_record_length}")
    # o.pointsCount = readAs(arraybuffer, Uint32Array, 32*3 + 11);
    (number_of_point_records,) = struct.unpack('<L', f.read(4)) #111
    print(f"* number_of_point_records {number_of_point_records}")
    for i in range(5):
        (number_of_points_by_return,) = struct.unpack('<L', f.read(4))
        print(f"number_of_points_by_return {i} {number_of_points_by_return}")
    # 131
    for i in ['x', 'y', 'z']:
        (scale_factor,) = struct.unpack('<d', f.read(8))
        print(f"{i}_scale_factor {scale_factor}")
    # 155
    for i in ['x', 'y', 'z']:
        (offset,) = struct.unpack('<d', f.read(8))
        print(f"{i}_offset {offset}")
    # 179
    for i in ['x', 'y', 'z']:
        (_max, _min) = struct.unpack('<dd', f.read(8*2))
        print(f"{i}_max {_max}")
        print(f"{i}_min {_min}")
    # 227
    (start_of_waveform_data_packet_record,) = struct.unpack('<Q', f.read(8)) #
    print(f"start_of_waveform_data_packet_record {start_of_waveform_data_packet_record}")
    print(f"current pos {f.tell()}")


if __name__ == '__main__':
    if len(sys.argv) == 2:
        file = sys.argv[1]
    else:
        exit()
    print(f"open {file}")
    f = open(file, 'rb')
    parse_header(f)
    print(f"close {file}")
    f.close()
