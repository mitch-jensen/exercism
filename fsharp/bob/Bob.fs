module Bob

let response (input: string): string =
    match input with
    | input when input.Contains("?") -> ""
    | input -> "Whatever."