package main

import "fmt"

// ServerState is a custom type based on int.
// We use this to create enum-like constants.
type ServerState int

// iota starts from 0 and increments automatically.
const (
	StateIdle ServerState = iota // 0
	StateConnected                // 1
	StateError                    // 2
	StateRetrying                 // 3
)

// Map to convert enum values to human-readable text.
var stateName = map[ServerState]string{
	StateIdle:      "idle",
	StateConnected: "connected",
	StateError:     "error",
	StateRetrying:  "retrying",
}

// String lets fmt.Println print the name instead of number.
// fmt uses String() automatically if it exists.
func (ss ServerState) String() string {
	return stateName[ss]
}

// transition defines how server moves between states.
func transition(s ServerState) ServerState {
	switch s {

	// idle → connected
	case StateIdle:
		return StateConnected

	// connected → idle
	// retrying → idle
	case StateConnected, StateRetrying:
		return StateIdle

	// error → stays error
	case StateError:
		return StateError

	// safety check for unknown values
	default:
		panic(fmt.Errorf("unknown state: %s", s))
	}
}

func main() {
	// Initial state
	ns := transition(StateIdle)
	fmt.Println(ns) // prints "connected"

	// Next transition
	ns2 := transition(ns)
	fmt.Println(ns2) // prints "idle"
}