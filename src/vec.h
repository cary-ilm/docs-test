//
// SPDX-License-Identifier: BSD-3-Clause
// Copyright Contributors to the OpenEXR Project.
// 

namespace Test {
    
template <class T> class Vec
{
  public:
    constexpr Vec (const Vec& v) noexcept;
    template <class S>  constexpr Vec (const Vec<S>& v) noexcept;
};

template <class T>
constexpr inline Vec<T>::Vec (const Vec& v) noexcept
{
}

template <class T> template <class S>
constexpr inline Vec<T>::Vec (const Vec<S>& v) noexcept
{
}

}



