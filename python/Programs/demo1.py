#demo usage

from wallaby import *
import os, sys

print "The courage of all human being - Space Battleship Yamato!"
enable_servo(0)
set_servo_position(0,100)
motor(0,50)
msleep(1000)
set_servo_position(0,300)
ao()
print """
    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU Affero General Public License as
    published by the Free Software Foundation, either version 3 of the
    License, or (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU Affero General Public License for more details.

    You should have received a copy of the GNU Affero General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>.
    """