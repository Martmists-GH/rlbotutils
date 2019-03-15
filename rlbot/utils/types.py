from math import sqrt, atan2, pi, cos, sin
from typing import Union, List

# Map boundaries
MIN_X, MAX_X = -4096.0, 4096.0
MIN_Y, MAX_Y = -5120.0, 5120.0
MIN_Z, MAX_Z = 0.0, 2044.0


class Vector:
    x: float
    y: float
    z: float

    def __init__(self, x: Union[List[float], float, 'Vector'] = 0,
                 y: float = 0, z: float = 0):
        if hasattr(x, "x"):
            self.x = x.x
            self.y = x.y
            self.z = x.z
        elif isinstance(x, list):
            self.x, self.y, self.z = x
        else:
            self.x: float = x
            self.y = y
            self.z = z

    def __repr__(self):
        return f"Vector({self.x}, {self.y}, {self.z})"

    # Properties

    @property
    def length(self) -> float:
        return sqrt(self.x**2 + self.y**2 + self.z**2)

    @property
    def normalized(self) -> 'Vector':
        if self.length == 0:
            return Vector(1, 1, 1)
        return self / self.length

    # Utilities

    def flat(self) -> 'Vector':
        return Vector(self.x, self.y, 0)
    
    def bounded(self) -> 'Vector':
        return Vector(min(max(MIN_X, self.x), MAX_X),
                      min(max(MIN_Y, self.y), MAX_Y),
                      min(max(MIN_Z, self.z), MAX_Z))

    def as_list(self) -> List[float]:
        return [self.x, self.y, self.z]

    def distance(self, other: 'Vector') -> float:
        return abs((self - other).length)

    def angle_2d(self, other: 'Vector') -> float:
        current_radians = atan2(self.y, -self.x)
        ideal_radians = atan2(other.y, -other.x)
        correction = ideal_radians - current_radians

        if abs(correction) > pi:
            if correction < 0:
                correction += 2 * pi
            else:
                correction -= 2 * pi

        return correction

    # Operator functions

    def __add__(self, other: 'Vector') -> 'Vector':
        return Vector(self.x + other.x,
                      self.y + other.y,
                      self.z + other.z)

    def __sub__(self, other: 'Vector') -> 'Vector':
        return Vector(self.x - other.x,
                      self.y - other.y,
                      self.z - other.z)

    def __mul__(self, other: Union[float, 'Vector']) -> 'Vector':
        if isinstance(other, Vector):
            return Vector(self.x * other.x,
                          self.y * other.y,
                          self.z * other.z)
        else:
            return Vector(self.x * other,
                          self.y * other,
                          self.z * other)

    __rmul__ = __mul__

    def __truediv__(self, other: Union[float, 'Vector']) -> 'Vector':
        if isinstance(other, Vector):
            assert other.length != 0
            return Vector(self.x / other.x,
                          self.y / other.y,
                          self.z / other.z)

        else:
            assert other != 0
            return Vector(self.x / other,
                          self.y / other,
                          self.z / other)

    def __neg__(self):
        return self * -1

    def __eq__(self, other: 'Vector') -> bool:
        return self.x == other.x and self.y == other.y and self.z == other.z


class Rotation:
    pitch: float
    yaw: float
    roll: float

    def __init__(self, pitch: Union[float, List[float], 'Rotation'] = 0,
                 yaw: float = 0, roll: float = 0):
        if hasattr(pitch, "yaw"):
            self.yaw = pitch.yaw
            self.pitch = pitch.pitch
            self.roll = pitch.roll
        elif isinstance(pitch, list):
            self.pitch, self.yaw, self.roll = pitch
        else:
            self.yaw = yaw
            self.pitch = pitch
            self.roll = roll

    # Properties

    @property
    def normalized(self) -> 'Rotation':
        return Rotation(self._normalize_axis(self.pitch),
                        self._normalize_axis(self.yaw),
                        self._normalize_axis(self.roll))

    # Utilities

    def as_vector(self) -> Vector:
        cos_pitch = cos(self.pitch)
        return Vector(cos(self.yaw) * cos_pitch,
                      sin(self.yaw) * cos_pitch,
                      sin(self.pitch))

    # Private functions

    @staticmethod
    def _normalize_axis(angle: float) -> float:
        angle &= 0xFFFF

        if angle > 32767:
            angle -= 0x10000

        return angle
