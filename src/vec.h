//
// SPDX-License-Identifier: BSD-3-Clause
// Copyright Contributors to the OpenEXR Project.
// 

namespace Test {
    
class Vec
{
  public:

    float x;

    constexpr Vec (const float x) noexcept;
    constexpr Vec (const Vec& v) noexcept;
};

constexpr inline Vec::Vec (const Vec& v) noexcept
    : x(v.x)
{
}

constexpr inline Vec::Vec (const float v) noexcept
    : x(v)
{
}

}



