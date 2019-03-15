package org.rlbot.utils.types

import kotlin.math.*

class Rotation(pitch: Number, yaw: Number, roll: Number){
    val pitch = pitch.toDouble()
    val yaw = yaw.toDouble()
    val roll = roll.toDouble()

    override fun toString(): String {
        return "Rotation($pitch, $yaw, $roll)"
    }

    // Properties

    val normalized: Rotation
        get() =
            Rotation(
                normalizeAxis(pitch),
                normalizeAxis(yaw),
                normalizeAxis(roll)
            )

    // Utilities

    fun fromList(arg: Array<Number>): Rotation {
        return Rotation(arg[0], arg[1], arg[2])
    }

    fun asArray(): Array<Double> {
        return arrayOf(pitch, yaw, roll)
    }

    fun asVector(): Vector {
        val cosPitch = cos(pitch)
        return Vector(
                cos(yaw) * cosPitch,
                sin(yaw) * cosPitch,
                sin(pitch)
        )
    }

    // Private functions

    private fun normalizeAxis(angle: Double): Double {
        val intAngle = angle.roundToInt()
        var norm = (0xFFFF and intAngle) + (angle - intAngle)

        if (norm > 0x7FFF){
            norm -= 0x10000
        }

        return norm
    }
}
