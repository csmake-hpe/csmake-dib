# <copyright>
# (c) Copyright 2017 Hewlett Packard Enterprise Development LP
#
# This program is free software: you can redistribute it and/or modify it
# under the terms of the GNU General Public License as published by the
# Free Software Foundation, either version 3 of the License, or (at your
# option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General
# Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
# </copyright>
from CsmakeModules.DIBRunPartsAspect import DIBRunPartsAspect

class SkipDIBScript(DIBRunPartsAspect):
    """Purpose: To completely skip a specified script
       Phases: build
       Flags:
           partOverride - the script proposed for skipping, 
                          e.g. 01-install-selinx"""

    def script_start__build(self, phase, options, step, stepoptions):
        self.flowcontrol.override('doNotStartScript', True, self)
        self.log.passed()
        return True

