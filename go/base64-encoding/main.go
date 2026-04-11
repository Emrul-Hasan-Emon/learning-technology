package main

import (
	b64 "encoding/base64"
	"fmt"
)

func main() {

	// ------------------------------------------------------------
	// 1️. RAW DATA
	// ------------------------------------------------------------
	fmt.Println("===== ORIGINAL DATA =====")

	data := "abc123!?$*&()'-=@~"
	fmt.Println("original:", data)

	// ------------------------------------------------------------
	// 2️. STANDARD BASE64 ENCODING
	// ------------------------------------------------------------
	fmt.Println("\n===== STANDARD BASE64 =====")

	sEnc := b64.StdEncoding.EncodeToString([]byte(data))
	fmt.Println("encoded:", sEnc)

	sDec, err := b64.StdEncoding.DecodeString(sEnc)
	if err != nil {
		fmt.Println("decode error:", err)
	}
	fmt.Println("decoded:", string(sDec))

	// ------------------------------------------------------------
	// 3️. URL SAFE BASE64 (IMPORTANT FOR APIs)
	// ------------------------------------------------------------
	fmt.Println("\n===== URL SAFE BASE64 =====")

	uEnc := b64.URLEncoding.EncodeToString([]byte(data))
	fmt.Println("url encoded:", uEnc)

	uDec, err := b64.URLEncoding.DecodeString(uEnc)
	if err != nil {
		fmt.Println("decode error:", err)
	}
	fmt.Println("url decoded:", string(uDec))

	// ------------------------------------------------------------
	// 4️. RAW BASE64 (NO PADDING = '=' removed)
	// ------------------------------------------------------------
	fmt.Println("\n===== RAW BASE64 =====")

	rawEnc := b64.RawStdEncoding.EncodeToString([]byte(data))
	fmt.Println("raw encoded:", rawEnc)

	rawDec, _ := b64.RawStdEncoding.DecodeString(rawEnc)
	fmt.Println("raw decoded:", string(rawDec))

	// ------------------------------------------------------------
	// 5️. URL SAFE WITHOUT PADDING
	// ------------------------------------------------------------
	fmt.Println("\n===== RAW URL SAFE =====")

	rawUrl := b64.RawURLEncoding.EncodeToString([]byte(data))
	fmt.Println("raw url encoded:", rawUrl)

	rawUrlDec, _ := b64.RawURLEncoding.DecodeString(rawUrl)
	fmt.Println("raw url decoded:", string(rawUrlDec))

	// ------------------------------------------------------------
	// 6️. REAL WORLD: EMAIL TOKEN STYLE ENCODING
	// ------------------------------------------------------------
	fmt.Println("\n===== TOKEN STYLE =====")

	token := "userId=101&role=admin"

	encodedToken := b64.StdEncoding.EncodeToString([]byte(token))
	fmt.Println("token encoded:", encodedToken)

	decodedToken, _ := b64.StdEncoding.DecodeString(encodedToken)
	fmt.Println("token decoded:", string(decodedToken))

	// ------------------------------------------------------------
	// 7️. IMAGE / FILE STYLE DATA (SIMULATION)
	// ------------------------------------------------------------
	fmt.Println("\n===== FILE DATA SIMULATION =====")

	fileData := []byte{72, 101, 108, 108, 111} // "Hello"

	fileEnc := b64.StdEncoding.EncodeToString(fileData)
	fmt.Println("file encoded:", fileEnc)

	fileDec, _ := b64.StdEncoding.DecodeString(fileEnc)
	fmt.Println("file decoded:", string(fileDec))

	// ------------------------------------------------------------
	// 8️. SAFE DECODING PATTERN
	// ------------------------------------------------------------
	fmt.Println("\n===== SAFE DECODE =====")

	input := "aGVsbG8=" // "hello"

	decoded, err := b64.StdEncoding.DecodeString(input)
	if err != nil {
		fmt.Println("invalid base64 input")
	} else {
		fmt.Println("safe decoded:", string(decoded))
	}

	// ------------------------------------------------------------
	// 9️. DIFFERENCE SUMMARY
	// ------------------------------------------------------------
	fmt.Println("\n===== BASE64 TYPES =====")

	fmt.Println("StdEncoding  -> normal base64 (+ /)")
	fmt.Println("URLEncoding  -> URL safe (- _)")
	fmt.Println("RawStd       -> no '=' padding")
	fmt.Println("RawURL       -> URL safe + no padding")
}