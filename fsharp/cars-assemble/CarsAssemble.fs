module CarsAssemble

let successRate (speed: int): float =
    if speed = 0 then 0.0
    elif speed <= 4 then 1.0
    elif speed <= 8 then 0.9
    elif speed = 9 then 0.8
    else 0.77

let productionRatePerHour (speed: int): float =
    let carsPerHour = 221
    float speed * float carsPerHour * successRate speed

let workingItemsPerMinute (speed: int): int =
    int (productionRatePerHour speed) / 60
