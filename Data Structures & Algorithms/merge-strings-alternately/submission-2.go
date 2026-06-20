func mergeAlternately(word1 string, word2 string) string {
	var builder strings.Builder

	builder.Grow(len(word1) + len(word2))

	i := 0
	for i < len(word1) && i < len(word2) {
		builder.WriteByte(word1[i])
		builder.WriteByte(word2[i])
		i++
	}

	builder.WriteString(word1[i:])
	builder.WriteString(word2[i:])

	return builder.String()
}
