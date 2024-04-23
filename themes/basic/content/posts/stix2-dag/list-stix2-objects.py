from typing import Iterable, Union
from stix2.datastore import DataSource
import json
from typing import Iterable, Union
from stix2.datastore import DataSource
from typing import Iterable
import os
import requests
from stix2 import (
    FileSystemSource,
    MemoryStore,
    MemorySource,
    CompositeDataSource,
)
from typing import Iterable, Union


CAPEC_URL = 'https://raw.githubusercontent.com/mitre/cti/master/capec/2.1/stix-capec.json'
ATTACK_ENTERPRISE_URL = 'https://github.com/mitre/cti/raw/master/enterprise-attack/enterprise-attack.json'
ATTACK_MOBILE_URL = 'https://github.com/mitre/cti/raw/master/mobile-attack/mobile-attack.json'
ATTACK_ICS_URL = 'https://github.com/mitre/cti/tree/master/ics-attack'
NIST_SP_800_53_URL = 'https://raw.githubusercontent.com/center-for-threat-informed-defense/attack-control-framework-mappings/main/frameworks/attack_12_1/nist800_53_r5/stix/nist800-53-r5-controls.json'
ATTACK_ENTERPRISE_TO_NIST_SP_800_53_URL = 'https://raw.githubusercontent.com/center-for-threat-informed-defense/attack-control-framework-mappings/main/frameworks/attack_12_1/nist800_53_r5/stix/nist800-53-r5-mappings.json'


def main():
    data_source = get_composite_stix2_data_source([
        CAPEC_URL,
        ATTACK_ENTERPRISE_URL,
        ATTACK_MOBILE_URL,
        ATTACK_ICS_URL,
        NIST_SP_800_53_URL,
        ATTACK_ENTERPRISE_TO_NIST_SP_800_53_URL,
    ])


def get_composite_stix2_data_source(
    data_sources: Union[str, DataSource, Iterable[Union[str, DataSource]]]
) -> Union[DataSource, CompositeDataSource]:
    if isinstance(data_sources, (str, DataSource)):
        return get_stix2_data_source(data_sources)
    else:
        data_sources = [get_stix2_data_source(ds) for ds in data_sources]
        composite_data_source = CompositeDataSource()
        composite_data_source.add_data_sources(data_sources)
        return composite_data_source
    

def get_stix2_data_source(path: str) -> DataSource:
    if os.path.exists(path):
        if os.path.isdir(path):
            return FileSystemSource(path)
        else:
            return _get_stix2_memory_source_from_file(path)
    elif path.startswith(("http://", "https://")):
        return _get_stix2_memory_source_from_web(path)
    else:
        raise ValueError(f"Invalid path: {path}")


def _get_stix2_memory_source_from_file(path: str) -> MemoryStore:
    with open(path, "rb") as file:
        stix_data = json.load(file)
        return MemorySource(stix_data=stix_data)


def _get_stix2_memory_source_from_web(url: str) -> MemoryStore:
    response = requests.get(url)
    response.raise_for_status()
    return MemorySource(response.json()["objects"])


if __name__ == "__main__":
    main()
