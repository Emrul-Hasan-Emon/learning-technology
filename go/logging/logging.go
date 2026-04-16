package main

import (
	"bytes"
	"context"
	"fmt"
	"log"
	"os"
	"io"

	"log/slog"
)

// ============================================================================
// Example 1: Standard Log Package
// ============================================================================
func example1_StandardLogger() {
	fmt.Println("\n=== Example 1: Standard Logger ===")

	// Basic logging
	log.Println("standard logger")
	log.Printf("formatted log: %s\n", "with values")
	log.Fatalln("this would exit the program (commented out)")
	// log.Fatalln("ERROR: Fatal error") // Uncomment to see it exit
}

// ============================================================================
// Example 2: Logger Flags
// ============================================================================
func example2_LoggerFlags() {
	fmt.Println("\n=== Example 2: Logger Flags ===")

	// Default flags (date and time)
	log.SetFlags(log.LstdFlags)
	log.Println("with LstdFlags (date + time)")

	// Add microseconds
	log.SetFlags(log.LstdFlags | log.Lmicroseconds)
	log.Println("with microseconds")

	// Add short file and line number
	log.SetFlags(log.LstdFlags | log.Lshortfile)
	log.Println("with file/line (shortfile)")

	// Add long file path
	log.SetFlags(log.LstdFlags | log.Llongfile)
	log.Println("with long file path")

	// Add UTC time
	log.SetFlags(log.LstdFlags | log.LUTC)
	log.Println("with UTC time")

	// Combination of flags
	log.SetFlags(log.Ldate | log.Ltime | log.Lmicroseconds | log.Lshortfile)
	log.Println("combining multiple flags")

	// Just time
	log.SetFlags(log.Ltime)
	log.Println("just time")
}

// ============================================================================
// Example 3: Custom Logger with Prefix
// ============================================================================
func example3_CustomLoggerWithPrefix() {
	fmt.Println("\n=== Example 3: Custom Logger with Prefix ===")

	// Create logger for INFO
	infoLog := log.New(os.Stdout, "[INFO] ", log.LstdFlags)
	infoLog.Println("This is an info message")

	// Create logger for ERROR
	errLog := log.New(os.Stderr, "[ERROR] ", log.LstdFlags|log.Lshortfile)
	errLog.Println("This is an error message")

	// Create logger for DEBUG
	debugLog := log.New(os.Stdout, "[DEBUG] ", log.Ltime|log.Lmicroseconds)
	debugLog.Println("This is a debug message")

	// Create logger for WARNING
	warnLog := log.New(os.Stdout, "[WARN] ", log.LstdFlags)
	warnLog.Println("This is a warning message")

	// Change prefix dynamically
	appLog := log.New(os.Stdout, "[APP] ", log.LstdFlags)
	appLog.Println("Before prefix change")

	appLog.SetPrefix("[APP-UPDATED] ")
	appLog.Println("After prefix change")
}

// ============================================================================
// Example 4: Logger Output to Different Destinations
// ============================================================================
func example4_LoggerDestinations() {
	fmt.Println("\n=== Example 4: Logger Output Destinations ===")

	// Logger to stdout
	stdoutLog := log.New(os.Stdout, "[STDOUT] ", log.LstdFlags)
	stdoutLog.Println("This goes to stdout")

	// Logger to stderr
	stderrLog := log.New(os.Stderr, "[STDERR] ", log.LstdFlags)
	stderrLog.Println("This goes to stderr")

	// Logger to buffer (in-memory)
	var buf bytes.Buffer
	bufLog := log.New(&buf, "[BUFFER] ", log.LstdFlags)
	bufLog.Println("This goes to buffer")
	bufLog.Println("Another buffer message")

	fmt.Println("\nBuffer contents:")
	fmt.Print(buf.String())

	// Logger to multiple destinations
	multiWriter := io.MultiWriter(os.Stdout, &buf)
	multiLog := log.New(multiWriter, "[MULTI] ", log.LstdFlags)
	multiLog.Println("This goes to both stdout and buffer")
}

// ============================================================================
// Example 5: Structured Logging with slog (Text Handler)
// ============================================================================
func example5_StructuredLoggingText() {
	fmt.Println("\n=== Example 5: Structured Logging (Text Handler) ===")

	// Create text handler
	opts := &slog.HandlerOptions{
		Level: slog.LevelDebug,
	}
	textHandler := slog.NewTextHandler(os.Stdout, opts)
	logger := slog.New(textHandler)

	// Log with key-value pairs
	logger.Info("User login", "username", "alice", "ip", "192.168.1.1")
	logger.Debug("Debug information", "status", "processing", "count", 42)
	logger.Error("An error occurred", "error", "connection timeout", "retry_count", 3)
}

// ============================================================================
// Example 6: Structured Logging with slog (JSON Handler)
// ============================================================================
func example6_StructuredLoggingJSON() {
	fmt.Println("\n=== Example 6: Structured Logging (JSON Handler) ===")

	// Create JSON handler
	opts := &slog.HandlerOptions{
		Level: slog.LevelDebug,
	}
	jsonHandler := slog.NewJSONHandler(os.Stdout, opts)
	logger := slog.New(jsonHandler)

	// Log with different levels
	logger.Debug("Debug message", "module", "database")
	logger.Info("Application started", "version", "1.0.0", "environment", "production")
	logger.Warn("Low memory", "available_mb", 256)
	logger.Error("Failed to connect", "host", "db.example.com", "port", 5432)
}

// ============================================================================
// Example 7: Log Levels with slog
// ============================================================================
func example7_LogLevels() {
	fmt.Println("\n=== Example 7: Log Levels ===")

	// Create logger with DEBUG level (shows all)
	opts := &slog.HandlerOptions{
		Level: slog.LevelDebug,
	}
	handler := slog.NewTextHandler(os.Stdout, opts)
	logger := slog.New(handler)

	logger.Debug("This is DEBUG level")
	logger.Info("This is INFO level")
	logger.Warn("This is WARN level")
	logger.Error("This is ERROR level")

	fmt.Println("\n--- With INFO level (DEBUG hidden) ---")
	// Create logger with INFO level (hides DEBUG)
	opts2 := &slog.HandlerOptions{
		Level: slog.LevelInfo,
	}
	handler2 := slog.NewTextHandler(os.Stdout, opts2)
	logger2 := slog.New(handler2)

	logger2.Debug("This DEBUG is hidden")
	logger2.Info("This INFO is shown")
	logger2.Warn("This WARN is shown")
	logger2.Error("This ERROR is shown")
}

// ============================================================================
// Example 8: Grouped Logging
// ============================================================================
func example8_GroupedLogging() {
	fmt.Println("\n=== Example 8: Grouped Logging ===")

	opts := &slog.HandlerOptions{
		Level: slog.LevelInfo,
	}
	handler := slog.NewTextHandler(os.Stdout, opts)
	logger := slog.New(handler)

	// Using With() to add context
	requestLogger := logger.With("request_id", "req-12345", "user_id", "usr-789")
	requestLogger.Info("Request received", "method", "GET", "path", "/api/users")
	requestLogger.Info("Processing request", "step", "validation")
	requestLogger.Info("Request completed", "status_code", 200, "duration_ms", 145)
}

// ============================================================================
// Example 9: WithGroup for nested context
// ============================================================================
func example9_WithGroup() {
	fmt.Println("\n=== Example 9: With Group ===")

	opts := &slog.HandlerOptions{
		Level: slog.LevelInfo,
	}
	handler := slog.NewTextHandler(os.Stdout, opts)
	logger := slog.New(handler)

	// Create grouped context
	userGroup := logger.WithGroup("user")
	userGroup.Info("Login", "name", "alice", "email", "alice@example.com")

	dbGroup := logger.WithGroup("database")
	dbGroup.Info("Query executed", "table", "users", "rows_affected", 1)

	// Nested groups
	requestGroup := logger.WithGroup("request")
	headerGroup := requestGroup.WithGroup("headers")
	headerGroup.Info("Header info", "content_type", "application/json", "auth", "Bearer token")
}

// ============================================================================
// Example 10: Context-based Logging
// ============================================================================
func example10_ContextLogging() {
	fmt.Println("\n=== Example 10: Context-based Logging ===")

	opts := &slog.HandlerOptions{
		Level: slog.LevelInfo,
	}
	handler := slog.NewTextHandler(os.Stdout, opts)
	logger := slog.New(handler)

	// Create context
	ctx := context.Background()

	// Log with context (using WithAttrs)
	logger.InfoContext(ctx, "Processing started", "operation", "data_sync")

	// Simulate some processing
	for i := 1; i <= 3; i++ {
		logger.InfoContext(ctx, "Processing item", "item_id", i, "status", "completed")
	}

	logger.InfoContext(ctx, "Processing finished", "total_items", 3)
}

// ============================================================================
// Example 11: Error Logging
// ============================================================================
func example11_ErrorLogging() {
	fmt.Println("\n=== Example 11: Error Logging ===")

	opts := &slog.HandlerOptions{
		Level: slog.LevelInfo,
	}
	handler := slog.NewTextHandler(os.Stdout, opts)
	logger := slog.New(handler)

	// Log error with details
	logger.Error("Failed to save user", 
		"user_id", 123,
		"error", "database connection timeout",
		"retry_attempt", 3,
		"action", "rollback",
	)

	logger.Error("API request failed",
		"endpoint", "/api/data",
		"status_code", 503,
		"error", "service unavailable",
		"response_time_ms", 5000,
	)
}

// ============================================================================
// Example 12: Multiple Loggers for Different Modules
// ============================================================================
func example12_MultipleLoggers() {
	fmt.Println("\n=== Example 12: Multiple Loggers ===")

	opts := &slog.HandlerOptions{
		Level: slog.LevelInfo,
	}

	// Logger for Database module
	dbHandler := slog.NewTextHandler(os.Stdout, opts)
	dbLogger := slog.New(dbHandler.WithAttrs([]slog.Attr{
		slog.String("module", "database"),
	}))

	// Logger for API module
	apiHandler := slog.NewTextHandler(os.Stdout, opts)
	apiLogger := slog.New(apiHandler.WithAttrs([]slog.Attr{
		slog.String("module", "api"),
	}))

	// Log from different modules
	dbLogger.Info("Connected to database", "host", "localhost")
	apiLogger.Info("Server started", "port", 8080)
	dbLogger.Info("Query executed", "query", "SELECT * FROM users")
	apiLogger.Info("Request processed", "method", "POST")
}

// ============================================================================
// Example 13: Custom Attributes
// ============================================================================
func example13_CustomAttributes() {
	fmt.Println("\n=== Example 13: Custom Attributes ===")

	opts := &slog.HandlerOptions{
		Level: slog.LevelInfo,
	}
	handler := slog.NewTextHandler(os.Stdout, opts)
	logger := slog.New(handler)

	// Log with various data types
	logger.Info("Application metrics",
		"uptime_seconds", 3600,
		"cpu_usage_percent", 45.5,
		"memory_mb", 512,
		"is_healthy", true,
		"errors_today", 0,
	)

	// Log complex data structure simulation
	logger.Info("Server config",
		"server_name", "web-server-1",
		"max_connections", 1000,
		"timeout_seconds", 30,
		"ssl_enabled", true,
		"version", "2.1.3",
	)
}

// ============================================================================
// Example 14: Conditional Logging
// ============================================================================
func example14_ConditionalLogging() {
	fmt.Println("\n=== Example 14: Conditional Logging ===")

	opts := &slog.HandlerOptions{
		Level: slog.LevelDebug,
	}
	handler := slog.NewTextHandler(os.Stdout, opts)
	logger := slog.New(handler)

	// Only log if level is enabled
	if logger.Enabled(context.Background(), slog.LevelDebug) {
		logger.Debug("Debug info", "query", "SELECT * FROM large_table")
	}

	if logger.Enabled(context.Background(), slog.LevelInfo) {
		logger.Info("Important info", "action", "user_registered")
	}

	// Change to higher level
	opts2 := &slog.HandlerOptions{
		Level: slog.LevelWarn,
	}
	handler2 := slog.NewTextHandler(os.Stdout, opts2)
	logger2 := slog.New(handler2)

	if logger2.Enabled(context.Background(), slog.LevelDebug) {
		logger2.Debug("This won't be logged")
	}

	if logger2.Enabled(context.Background(), slog.LevelWarn) {
		logger2.Warn("This will be logged")
	}
}

// ============================================================================
// Example 15: Performance - Buffer Logging
// ============================================================================
func example15_BufferLogging() {
	fmt.Println("\n=== Example 15: Buffer Logging ===")

	// Create buffer for high-speed logging
	var buf bytes.Buffer
	opts := &slog.HandlerOptions{
		Level: slog.LevelInfo,
	}
	handler := slog.NewTextHandler(&buf, opts)
	logger := slog.New(handler)

	// Fast logging to buffer
	for i := 1; i <= 5; i++ {
		logger.Info("Event processed", "event_id", i, "timestamp", "2024-01-01T10:00:00Z")
	}

	fmt.Println("Buffered logs:")
	fmt.Println(buf.String())
}

// ============================================================================
// Example 16: File Logging
// ============================================================================
func example16_FileLogging() {
	fmt.Println("\n=== Example 16: File Logging ===")

	// Create or open log file
	file, err := os.OpenFile("app.log", os.O_CREATE|os.O_WRONLY|os.O_APPEND, 0666)
	if err != nil {
		fmt.Println("Error opening log file:", err)
		return
	}
	defer file.Close()

	// Create logger that writes to file
	fileLogger := log.New(file, "[FILE] ", log.LstdFlags|log.Lshortfile)
	fileLogger.Println("Log entry written to file")
	fileLogger.Printf("Formatted log with data: %v\n", map[string]interface{}{
		"user_id": 123,
		"action":  "login",
	})

	fmt.Println("Logs written to app.log")

	// Clean up - remove test log file
	os.Remove("app.log")
}

// ============================================================================
// Main Function
// ============================================================================
func main() {
	fmt.Println("=============== Go Logging Examples ===============")

	example1_StandardLogger()
	example2_LoggerFlags()
	example3_CustomLoggerWithPrefix()
	example4_LoggerDestinations()
	example5_StructuredLoggingText()
	example6_StructuredLoggingJSON()
	example7_LogLevels()
	example8_GroupedLogging()
	example9_WithGroup()
	example10_ContextLogging()
	example11_ErrorLogging()
	example12_MultipleLoggers()
	example13_CustomAttributes()
	example14_ConditionalLogging()
	example15_BufferLogging()
	example16_FileLogging()

	fmt.Println("\n=============== Examples Complete ===============")
}