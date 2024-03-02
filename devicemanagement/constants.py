from enum import Enum

class Device:
    def __init__(self, uuid: int, name: str, version: str, ipad: bool):
        self.uuid = uuid
        self.name = name
        self.version = version
        self.ipad = ipad

class Version:
    def __init__(self, major: int, minor: int = 0, patch: int = 0):
        self.major = major
        self.minor = minor
        self.patch = patch

    def __init__(self, ver: str):
        nums: list[str] = ver.split(".")
        self.major = int(nums[0])
        self.minor = int(nums[1]) if len(nums) > 1 else 0
        self.patch = int(nums[2]) if len(nums) > 2 else 0

    # Comparison Functions
    def compare_to(self, other) -> int:
        if self.major > other.major:
            return 1
        elif self.major < other.major:
            return -1
        if self.minor > other.minor:
            return 1
        elif self.minor < other.minor:
            return -1
        if self.patch > other.patch:
            return 1
        elif self.patch < other.patch:
            return -1
        return 0
        
    def __gt__(self, other) -> bool:
        return self.compare_to(other) == 1
    def __ge__(self, other) -> bool:
        comp: int = self.compare_to(other)
        return comp == 0 or comp == 1
    
    def __lt__(self, other) -> bool:
        return self.compare_to(other) == -1
    def __le__(self, other) -> bool:
        comp: int = self.compare_to(other)
        return comp == 0 or comp == -1
    
    def __eq__(self, other) -> bool:
        return self.compare_to(other) == 0
    
class Tweak(Enum):
    springboard_options = 'SpringboardOptions'