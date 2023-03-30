# SPDX-License-Identifier: BSD-3-Clause
# Copyright (c) Contributors to the OpenEXR Project.

# We require this to get object library link library support
cmake_minimum_required(VERSION 3.12)

project(docs-test VERSION 42.0)

option(BUILD_DOCS "Set ON to build html documentation")
if (BUILD_DOCS)
  option(INSTALL_DOCS "Set ON to install html documentation" ON)
  add_subdirectory(docs)
endif()

