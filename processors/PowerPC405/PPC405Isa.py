# -*- coding: iso-8859-1 -*-
####################################################################################
#         ___        ___           ___           ___
#        /  /\      /  /\         /  /\         /  /\
#       /  /:/     /  /::\       /  /::\       /  /::\
#      /  /:/     /  /:/\:\     /  /:/\:\     /  /:/\:\
#     /  /:/     /  /:/~/:/    /  /:/~/::\   /  /:/~/:/
#    /  /::\    /__/:/ /:/___ /__/:/ /:/\:\ /__/:/ /:/
#   /__/:/\:\   \  \:\/:::::/ \  \:\/:/__\/ \  \:\/:/
#   \__\/  \:\   \  \::/~~~~   \  \::/       \  \::/
#        \  \:\   \  \:\        \  \:\        \  \:\
#         \  \ \   \  \:\        \  \:\        \  \:\
#          \__\/    \__\/         \__\/         \__\/
#
#   This file is part of TRAP.
#
#   TRAP is free software; you can redistribute it and/or modify
#   it under the terms of the GNU Lesser General Public License as published by
#   the Free Software Foundation; either version 2 of the License, or
#   (at your option) any later version.
#
#   This program is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#   GNU Lesser General Public License for more details.
#
#   You should have received a copy of the GNU Lesser General Public License
#   along with this TRAP; if not, write to the
#   Free Software Foundation, Inc.,
#   51 Franklin Street, Fifth Floor, Boston, MA  02110-1301  USA.
#   or see <http://www.gnu.org/licenses/>.
#
#   (c) Luca Fossati, fossati@elet.polimi.it
#
####################################################################################



# Lets first of all import the necessary files for the
# creation of the processor
import trap
import cxx_writer
from PPC405Coding import *
from PPC405Methods import *

# ISA declaration: it is the container for all the single instructions
isa = trap.ISA()
#ADD
opCode = cxx_writer.writer_code.Code("""
rt = (int)rb + (int)ra;
""")
add_Instr = trap.Instruction('ADD', True)
add_Instr.setMachineCode(oper_X0form_1, {'primary_opcode': [0,1,1,1,1,1], 'xo': [1,0,0,0,0,1,0,1,0]}, ('add r', '%rt', ' r', '%ra', ' r', '%rb'))
add_Instr.setCode(opCode,'execute')
add_Instr.addBehavior(IncrementPC, 'execute')
add_Instr.addTest({'rt': 3, 'ra': 1, 'rb': 2}, {'GPR[1]': 4, 'GPR[2]': 6, 'GPR[3]': 0xfffff, 'PC':0x0, 'GPR[4]':0x00000000, 'GPR[5]':0xffffffff}, {'GPR[3]': 10, 'PC':0x4, 'GPR[4]':0x00000000})
isa.addInstruction(add_Instr)
#ADDC
opCode = cxx_writer.writer_code.Code("""
rt = (int)rb + (int)ra;
if ((int)rb + (int)ra>exp(2,32)-1) {
	XER[CA] = 1;
}
else {
	XER[CA] = 0;
}
""")
addc_Instr = trap.Instruction('ADDC', True)
addc_Instr.setMachineCode(oper_X0form_1, {'primary_opcode': [0,1,1,1,1,1], 'xo': [0,0,0,0,0,1,0,1,0]}, ('add r', '%rt', ' r', '%ra', ' r', '%rb'))
addc_Instr.setCode(opCode,'execute')
addc_Instr.addBehavior(IncrementPC, 'execute')
addc_Instr.addTest({'rt': 3, 'ra': 1, 'rb': 2}, {'GPR[1]': 4, 'GPR[2]': 6, 'GPR[3]': 0xfffff, 'PC':0x0, 'GPR[4]':0x00000000, 'GPR[5]':0xffffffff}, {'GPR[3]': 10, 'PC':0x4, 'GPR[4]':0x00000000})
isa.addInstruction(addc_Instr)
#ADDE
opCode = cxx_writer.writer_code.Code("""
rt = (int)rb + (int)ra + XER[CA];
if ((int)rb + (int)ra + XER[CA] > exp(2,32)-1) {
	XER[CA] = 1;
}
else {
	XER[CA] = 0;
}
""")
adde_Instr = trap.Instruction('ADDE', True)
adde_Instr.setMachineCode(oper_X0form_1, {'primary_opcode': [0,1,1,1,1,1], 'xo': [0,1,0,0,0,1,0,1,0]}, ('add r', '%rt', ' r', '%ra', ' r', '%rb'))
adde_Instr.setCode(opCode,'execute')
adde_Instr.addBehavior(IncrementPC, 'execute')
adde_Instr.addTest({'rt': 3, 'ra': 1, 'rb': 2}, {'GPR[1]': 4, 'GPR[2]': 6, 'GPR[3]': 0xfffff, 'PC':0x0, 'GPR[4]':0x00000000, 'GPR[5]':0xffffffff}, {'GPR[3]': 10, 'PC':0x4, 'GPR[4]':0x00000000})
isa.addInstruction(adde_Instr)

#ADDI
opCode = cxx_writer.writer_code.Code("""
if(ra == 0){
	rt = 0 + exts(IM);
}
else{
	(rt) = (int)(ra) + exts(IM);
}
""")
addi_Instr = trap.Instruction('ADDI', True)
addi_Instr.setMachineCode(oper_Dform_2 , {'primary_opcode': [0,1,1,1,1,1] }, ('add r', '%rt', ' r', '%ra'))
addi_Instr.setCode(opCode,'execute')
addi_Instr.addBehavior(IncrementPC, 'execute')
#addi_Instr.addTest({'rt': 3, 'ra': 1}, {'GPR[1]': 4, 'GPR[2]': 6, 'GPR[3]': 0xfffff, 'PC':0x0, 'GPR[4]':0x00000000, 'GPR[5]':0xffffffff}, {'GPR[3]': 10, 'PC':0x4, 'GPR[4]':0x00000000})
isa.addInstruction(addi_Instr)

