import xmltodict
from pathlib import Path
from homework_11.my_streem_logger import logger

path_to_xml: Path = Path("xml_files/groups.xml")


def convert_xml_to_dict(xml_path) -> dict:
    with open(xml_path, "r") as file:
        xml_string: str = file.read()
        xml_converted: dict = xmltodict.parse(xml_string)
        return xml_converted


data: dict = convert_xml_to_dict(path_to_xml)

groups: list[dict] = data["groups"]["group"]


def get_incoming_by_group_number(xml_data, number_in_group):
    for xml_group in xml_data:
        number = xml_group.get("number")
        if str(number) == str(number_in_group):
            timing_exbyte = xml_group.get("timingExbytes")
            if "incoming" in timing_exbyte:
                incoming_number = timing_exbyte["incoming"]
                logger.info(f"incoming number in group with number: {number_in_group}, is {incoming_number}")


if __name__ == "__main__":
    get_incoming_by_group_number(groups, 0)
