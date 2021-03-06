/***************************************************************************//**
*
*  _/_/_/_/_/  _/_/_/           _/        _/_/_/
*     _/      _/    _/        _/_/       _/    _/
*    _/      _/    _/       _/  _/      _/    _/
*   _/      _/_/_/        _/_/_/_/     _/_/_/
*  _/      _/    _/     _/      _/    _/
* _/      _/      _/  _/        _/   _/
*
* @file     exec_loader.hpp
* @brief    This file is part of the TRAP runtime library.
* @details
* @author   Luca Fossati
* @author   Lillian Tadros (Technische Universitaet Dortmund)
* @date     2008-2013 Luca Fossati
*           2015-2016 Technische Universitaet Dortmund
* @copyright
*
* This file is part of TRAP.
*
* TRAP is free software; you can redistribute it and/or modify
* it under the terms of the GNU Lesser General Public License as
* published by the Free Software Foundation; either version 3 of the
* License, or (at your option) any later version.
*
* This program is distributed in the hope that it will be useful,
* but WITHOUT ANY WARRANTY; without even the implied warranty of
* MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
* GNU Lesser General Public License for more details.
*
* You should have received a copy of the GNU Lesser General Public
* License along with this program; if not, write to the
* Free Software Foundation, Inc.,
* 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301  USA
* or see <http://www.gnu.org/licenses/>.
*
* (c) Luca Fossati, fossati@elet.polimi.it, fossati.l@gmail.com
*
*******************************************************************************/

#ifndef TRAP_EXEC_LOADER_H
#define TRAP_EXEC_LOADER_H

#include "elf_frontend.hpp"

extern "C" {
#include <gelf.h>
}

#include <string>
#include <iostream>
#include <fstream>

namespace trap {

/**
 * @brief ExecLoader
 */
class ExecLoader {
  /// @name Constructors and Destructors
  /// @{

  public:
  /// Initializes the loader of executable files by creating the corresponding
  /// ELF image of the executable file specified as parameter.
  ExecLoader(std::string filename, bool plain_file = false);

  ~ExecLoader();

  /// @} Constructors and Destructors
  /// ------------------------------------------------------------------------
  /// @name Interface Methods
  /// @{

  public:
  /// Returns the entry point of the loaded program (usually the same as the
  /// program start address, but not always).
  unsigned get_program_start();

  /// Returns the dimension of the loaded program.
  unsigned get_program_dim();

  /// Returns the start address of the program being loaded (the lowest address
  /// of the program).
  unsigned get_data_start();

  /// Returns a pointer to the array containing the program data.
  unsigned char* get_program_data();

  /// @} Interface Methods
  /// ------------------------------------------------------------------------
  /// @name Data
  /// @{

  private:
  /// Reference to the main elf parser.
  ELFFrontend* elf_frontend;
  /// Binary image of the application according to the BFD format.
  std::ifstream plain_exec_file;
  /// Specifies whether a normal binary file (ELF; COFF, etc.) or a plain file
  /// (just the opcodes of the instructions) was used.
  bool plain_file;
  /// Data of the program to be executed in case it is a simply sequence of
  /// instructions (i.e. not an ELF structured file).
  unsigned char* program_data;

  /// @} Data
}; // class ExecLoader

} // namespace trap

/// ****************************************************************************
#endif // TRAP_EXEC_LOADER_H
