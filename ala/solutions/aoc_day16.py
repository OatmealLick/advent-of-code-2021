from ala.solutions.utils import read_str_input


class HexadecimalMessageDecoder:
    def __init__(self):
        self.versions_sum = 0

    def add_up_versions_sum(self, message):
        message = bin(int(message, 16))[2:].zfill(len(message) * 4)
        while message:
            message = self.parse_package(message)
        return self.versions_sum

    def parse_package(self, message):
        if not message or len(message) < 7:
            return

        packet_version = int(message[:3], 2)
        packet_type_id = int(message[3:6], 2)
        print(packet_version)
        self.versions_sum += packet_version
        message = message[6:]

        if packet_type_id == 4:
            literal_value, message = self._get_literal_value(message)
            return message
        else:
            length_type_id = int(message[0])
            message = message[1:]
            if length_type_id == 0:
                total_length_of_bits = int(message[:15], 2)
                message, rest_of_message = message[15:15 + total_length_of_bits], message[15 + total_length_of_bits:]
                while message:
                    message = self.parse_package(message)
                return rest_of_message
            elif length_type_id == 1:
                number_of_subpackets = int(message[:11], 2)
                message = message[11:]
                while number_of_subpackets:
                    if message:
                        message = self.parse_package(message)
                    number_of_subpackets -= 1
                return message

    def _get_literal_value(self, message):
        literal_value = ''
        if not message:
            return None, message
        pointer = 0
        keep_reading = 1
        while keep_reading:
            keep_reading = int(message[pointer])
            pointer += 1
            literal_value += message[pointer:pointer + 4]
            pointer += 4
        message = message[pointer:]
        return int(literal_value, 2), message


if __name__ == '__main__':
    input_path = '../inputs/test_aoc_day16.txt'
    message = read_str_input(input_path)[0]

    hmd = HexadecimalMessageDecoder()
    print(hmd.add_up_versions_sum(message))
