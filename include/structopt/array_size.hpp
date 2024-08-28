
#pragma once
#include <array>
#include <cstdint>

namespace structopt {

template <typename> struct array_size;
template <typename T, std::size_t N> struct array_size<std::array<T, N>> {
  static std::size_t const size = N;
};

} // namespace structopt
