# Prompt Comparison – Extract Name, Date, Location

## Goal
Extract `name`, `date`, and `location` from a paragraph using a clear prompt, then compare results between GPT (OpenAI) and Claude (Anthropic), and describe how to normalize the output.

---

## Prompt used:
```
Extract the name of the main participant, the event date, and the primary location of the event from the following paragraph.  
Return only the result in JSON format with fields: name, date, location.

Paragraph:
{{text}}
```

---

## Example 1 – Simple sentence

### Input:
> Nhien will attend the AI Summit on September 1st in Singapore

### Expected Output:
```json
{
  "name": "Nhien",
  "date": "September 1st",
  "location": "Singapore"
}
```

### GPT vs Claude:
- GPT: Correct. Valid JSON.
- Claude: Correct. JSON matches GPT.

No significant difference as the sentence is simple and information is clear.

---

## Example 2 – Complex sentence, multiple locations and time logic

### Input:
> Dr. Lee confirmed that he would be attending the Climate Technology Forum in Ho Chi Minh City from October 3rd to 5th, 2025, after returning from a short trip to Tokyo.

### Expected Output:
```json
{
  "name": "Dr. Lee",
  "date": "October 3rd to 5th, 2025",
  "location": "Ho Chi Minh City"
}
```

### GPT vs Claude:
- GPT: Correct. Ignores Tokyo, selects Ho Chi Minh City.
- Claude: Correct. Sometimes rewrites as "3–5 Oct" if format is not strictly required.

Both models handle complex logic well. Claude tends to "normalize" dates more if the prompt is not strict about format.

---

## Output Normalization

Although the results are correct, for use in automated systems, you should:

- Use `json.loads(response)` to ensure valid JSON format
- Normalize `date` to ISO format (`YYYY-MM-DD`) using `dateutil` or `datetime.strptime()` if needed for queries
- Clean `name`/`location`: strip whitespace, capitalize first letter if needed

---

## Summary

- Both GPT and Claude provide good results if the prompt is clear
- Claude sometimes "explains more" if not strictly required
- The best prompt should:
  - Be clear about the format
  - Require "JSON only"
  - Avoid letting the model "freely" interpret too much

---