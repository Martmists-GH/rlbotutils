package org.rlbot.utils.types

import kotlin.math.*


class Vector(x: Number, y: Number, z: Number){
    val x = x.toDouble()
    val y = y.toDouble()
    val z = z.toDouble()

    private val MIN_X = -4096.0
    private val MAX_X = 4096.0
    private val MIN_Y = -5120.0
    private val MAX_Y = 5120.0
    private val MIN_Z = 0.0
    private val MAX_Z = 2044.0

    override fun toString(): String {
        return "Vector($x, $y, $z)"
    }

    // Properties

    val length: Double
            get() = sqrt(this.x.pow(2) + this.y.pow(2) + this.z.pow(2))

    val normalized: Vector
            get() =
                if (this.length == 0.0) {
                    Vector(1, 1, 1)
                } else { this / this.length }

    // Utilities

    fun fromList(arg: Array<Number>): Vector {
        return Vector(arg[0], arg[1], arg[2])
    }

    fun asArray(): Array<Double> {
        return arrayOf(x, y, z)
    }

    fun bounded(): Vector {
        return Vector(
                min(max(x, MIN_X), MAX_X),
                min(max(y, MIN_Y), MAX_Y),
                min(max(z, MIN_Z), MAX_Z)
        )
    }

    fun distance(other: Vector): Double {
        return abs((this - other).length)
    }

    fun angle2D(other: Vector): Double {
        val currentRadians = atan2(y, -x)
        val idealRadians = atan2(other.y, -other.x)
        var correction = idealRadians - currentRadians

        if (abs(correction) > PI){
            if (correction < 0){
                correction += 2 * PI
            } else {
                correction -= 2 * PI
            }
        }

        return correction
    }

    // Operator functions

    operator fun plus(other: Vector): Vector {
        return Vector(
                x + other.x,
                y + other.y,
                z + other.z
        )
    }

    operator fun minus(other: Vector): Vector {
        return Vector(
                x - other.x,
                y - other.y,
                z - other.z
        )
    }

    operator fun times(other: Number): Vector {
        return Vector(
                x * other.toDouble(),
                y * other.toDouble(),
                z * other.toDouble()
        )
    }

    operator fun times(other: Vector): Vector {
        return Vector(
                x * other.x,
                y * other.y,
                z * other.z
        )
    }

    operator fun div(other: Number): Vector {
        assert(other != 0)
        return Vector(
                x * other.toDouble(),
                y * other.toDouble(),
                z * other.toDouble()
        )
    }

    operator fun unaryMinus(): Vector {
        return this * -1
    }

    override operator fun equals(other: Any?): Boolean {
        if (other is Vector){
            return x == other.x && y == other.y && z == other.z
        }
        return false
    }
}
