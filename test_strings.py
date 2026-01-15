def test_uppercase():
    assert "hello".upper() == "HELLO"

def test_lowercase():
    assert "WORLD".lower() == "world"
```

**`requirements.txt`**
```
pytest
```

---

## Part 3: Create the Jenkins Job

1. **Open Jenkins** → Click **New Item**
2. Enter a name (e.g., `SQMA_Tests`) → Select **Freestyle project** → Click **OK**

3. **Add the Parameter** (this is the key part!):
   - Check ✅ **This project is parameterized**
   - Click **Add Parameter** → **Choice Parameter**
   - Name: `TEST_CHOICE`
   - Choices (one per line):
```
     test_math
     test_strings
     all_tests
