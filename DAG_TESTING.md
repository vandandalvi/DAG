# 🧪 Testing DAG Validation

## Test Cases for Backend

### ✅ Test 1: Valid DAG (Linear Chain)
```
Input → LLM → Output
```
**Expected:** is_dag: true ✓

### ✅ Test 2: Valid DAG (Branching)
```
     ┌→ LLM1 → Output1
Input
     └→ LLM2 → Output2
```
**Expected:** is_dag: true ✓

### ✅ Test 3: Valid DAG (Merging)
```
Input1 ─┐
        ├→ LLM → Output
Input2 ─┘
```
**Expected:** is_dag: true ✓

### ❌ Test 4: INVALID - Simple Cycle (Triangle)
```
A → B → C → A (back to start)
```
**Expected:** is_dag: false ✗

### ❌ Test 5: INVALID - Four-Node Cycle
```
A → B
↑   ↓
D ← C
```
**Expected:** is_dag: false ✗

### ❌ Test 6: INVALID - Self Loop
```
A → A (connects to itself)
```
**Expected:** is_dag: false ✗

---

## 📋 Step-by-Step: How to Create Test 4 (Triangle Cycle)

### Using Input, LLM, and Output nodes:

1. **Drag nodes onto canvas:**
   - Drag **Input** node (let's call it A)
   - Drag **LLM** node (let's call it B)  
   - Drag **Output** node (let's call it C)

2. **Position them in a triangle:**
   ```
   A (Input)
   ↓
   B (LLM)
   ↓
   C (Output)
   ```

3. **Create the cycle:**
   - **Connection 1:** Drag from Input's output handle → LLM's input handle
   - **Connection 2:** Drag from LLM's output handle → Output's input handle
   - **Connection 3 (THE CYCLE):** Drag from Output's output handle → back to Input's input handle
   
   This creates: Input → LLM → Output → Input (CYCLE!)

4. **Click "Submit Pipeline"**

5. **Result should show:**
   - Number of Nodes: 3
   - Number of Edges: 3
   - **Is Valid DAG: ✗ No** (RED)
   - **Warning:** "⚠️ Warning: Your pipeline contains cycles..."

---

## ⚠️ Problem: Output Node Might Not Have Output Handle

If the Output node doesn't have an output handle (since it's usually a terminal node), you can:

### **Alternative: Use Text Nodes**

Text nodes have both input AND output handles!

1. **Drag 3 Text nodes:**
   - Text1
   - Text2
   - Text3

2. **Create cycle:**
   - Text1 → Text2
   - Text2 → Text3
   - Text3 → Text1 (CYCLE!)

3. **Submit** - Should show: is_dag: false ✗

---

## 🔍 Why Your Tests All Show "Yes"

If you're only creating:
- **Linear chains** (A → B → C)
- **Trees** (branching but no loops)
- **DAGs** (merging but no cycles)

Then **"✓ Yes" is CORRECT!** The backend is working properly.

---

## ✅ Quick Test Right Now

1. **Open:** http://localhost:3000
2. **Drag 3 Text nodes** onto the canvas
3. **Connect them in a triangle:**
   - Click and drag from Text1's right handle → Text2's left handle
   - Click and drag from Text2's right handle → Text3's left handle  
   - Click and drag from Text3's right handle → **back to Text1's left handle**
4. **Click Submit Pipeline**
5. **You should see:** Is Valid DAG: ✗ No (with red color)

---

## 🎬 For Your Screen Recording

When you demonstrate the cycle detection:

**Say this:**
"Now let me test the cycle detection. I'll create a cycle..."

**Do this:**
1. Use 3 Text nodes (they have both input and output)
2. Connect: Text1 → Text2 → Text3 → Text1
3. Click Submit
4. Point to the red "✗ No" and say: "See, it correctly detects this is not a DAG because it contains a cycle."

---

## 💡 Pro Tip for Demo

Show **both** cases in your video:

1. **First:** Create valid DAG (Input → LLM → Output)
   - Submit → Show "✓ Yes" in green

2. **Then:** Create cycle (3 Text nodes in a loop)
   - Submit → Show "✗ No" in red with warning

This proves your backend validation works both ways!

---

**Try creating the Text node cycle right now and test it!** 🚀
