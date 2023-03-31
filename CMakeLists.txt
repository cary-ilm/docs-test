# SPDX-License-Identifier: BSD-3-Clause
# Copyright (c) Contributors to the OpenEXR Project.

# We require this to get object library link library support
cmake_minimum_required(VERSION 3.12)

project(docs-test VERSION 42.0)

if(POLICY CMP0074)
  # enable find_package(<Package>) to use <Package>_ROOT as a hint
  cmake_policy(SET CMP0074 NEW)
endif()

if(POLICY CMP0077)
  # enable variables set outside to override options
  cmake_policy(SET CMP0077 NEW)
endif()

option(BUILD_DOCS "Set ON to build html documentation" ON)
if (BUILD_DOCS)

  find_package(Python3 COMPONENTS Interpreter)
  if (NOT Python3_FOUND)
    message(STATUS "Python3 not found: skipping bin tests")
    return()
  endif()

  option(INSTALL_DOCS "Set ON to install html documentation" ON)
  add_subdirectory(docs)
endif()

