//
// Created by Syl Morrison on 22/07/2023.
//
#include "../pow.hpp"
#include <catch2/benchmark/catch_benchmark.hpp>
#include <catch2/catch_test_macros.hpp>
#include <catch2/matchers/catch_matchers.hpp>
#include <catch2/matchers/catch_matchers_floating_point.hpp>
namespace fastmaths::tests {

    float getDeviationFromStl(float x, float y, const std::function<float(float, float)>& toTest) {
        auto stlRes = std::powf(x, y);
        auto testedRes = toTest(x, y);
        auto delta = std::abs(testedRes - stlRes);
        return delta;
    }

    TEST_CASE("Test fast::pow::stl", "[stl]") {
        REQUIRE_THAT(fast::pow::stl(4.0f, 2.0f), Catch::Matchers::WithinRel(16.0f));
        BENCHMARK("fast::pow::stl") {
            for(auto i = 0; i < 100; ++i) {
                volatile auto res = fast::pow::stl(2.0f, static_cast<float>(i));
            }
        };
    }
    TEST_CASE("Test fast::pow::ekmett_fast", "[ekmett_fast]") {
        // Need to get the deviation from the STL one..


        REQUIRE_THAT(fast::pow::ekmett_fast(4.0f, 2.0f), Catch::Matchers::WithinRel(16.0f));
        BENCHMARK("fast::pow::ekmett_fast") {
            for(auto i = 0; i < 100; ++i) {
                volatile auto res = fast::pow::ekmett_fast(2.0f, static_cast<float>(i));
            }
        };
    }
}