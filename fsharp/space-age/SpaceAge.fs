module SpaceAge

open Microsoft.FSharp.Data.UnitSystems.SI.UnitNames

// TODO: define the Planet type
type Planet =
    | Mercury
    | Venus
    | Earth
    | Mars
    | Jupiter
    | Saturn
    | Uranus
    | Neptune
    
let convertSecondsToEarthYears (time: int64): float =
    float time / 31557600.0

let age (planet: Planet) (seconds: int64): float =
    let earthYears = convertSecondsToEarthYears seconds
    match planet with
    | Mercury -> earthYears / 0.2408467 
    | Venus -> earthYears / 0.61519726
    | Earth -> earthYears
    | Mars -> earthYears / 1.8808158
    | Jupiter -> earthYears / 11.862615
    | Saturn -> earthYears / 29.447498
    | Uranus -> earthYears / 84.016846
    | Neptune -> earthYears / 164.79132