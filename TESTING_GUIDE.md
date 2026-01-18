# 🎯 VectorShift Assessment - Quick Test Guide

## ✅ Setup Complete!

Both servers are now running:
- **Frontend**: http://localhost:3000
- **Backend**: http://localhost:8000

---

## 🧪 Testing Checklist

### Part 1: Node Abstraction - Test All 9 Nodes

#### Original 4 Nodes (Refactored)
1. ✅ **Input Node**
   - Drag onto canvas
   - Change name and type (Text/File)
   - Verify output handle on right
   - Click × button to delete

2. ✅ **LLM Node**
   - Drag onto canvas
   - Verify 2 input handles (system, prompt)
   - Verify 1 output handle (response)
   - Click × button to delete

3. ✅ **Output Node**
   - Drag onto canvas
   - Change name and type (Text/Image)
   - Verify input handle on left

4. ✅ **Text Node** (Enhanced - See Part 3)
   - Drag onto canvas
   - Type text with variables
   - Watch node expand

#### New 5 Nodes
5. ✅ **Filter Node**
   - Drag onto canvas
   - Select condition (Contains, Equals, Starts With, Ends With)
   - Enter filter value
   - Verify 1 input, 2 outputs (passed, filtered)

6. ✅ **Transform Node**
   - Drag onto canvas
   - Select operation (Uppercase, Lowercase, Trim, Reverse)
   - Verify 1 input, 1 output

7. ✅ **API Node**
   - Drag onto canvas
   - Select HTTP method (GET, POST, PUT, DELETE)
   - Enter URL and headers
   - Verify 1 input (body), 2 outputs (response, error)

8. ✅ **Conditional Node**
   - Drag onto canvas
   - Select operator (>, <, ==, !=)
   - Enter threshold value
   - Verify 1 input, 2 outputs (true, false)

9. ✅ **Aggregator Node**
   - Drag onto canvas
   - Select operation (Concatenate, Sum, Average, Merge Objects)
   - Enter separator (for concat)
   - Verify 3 inputs, 1 output

---

### Part 2: Styling - Visual Verification

1. ✅ **Toolbar**
   - Modern design with title and icon
   - Hover effects on draggable nodes
   - Clean layout with proper spacing

2. ✅ **Canvas**
   - Light background with grid
   - Smooth animations when dragging
   - Controls and minimap styled

3. ✅ **Nodes**
   - Each node has unique color
   - Rounded corners and shadows
   - Hover effect (lift up)
   - Selected state (blue border)

4. ✅ **Edges**
   - Smooth curved lines
   - Animated flow
   - Arrow markers

5. ✅ **Submit Button**
   - Gradient background
   - Hover animation
   - Loading state when clicked

---

### Part 3: Text Node Logic - Interactive Testing

#### Test 1: Dynamic Sizing (Width)
```
1. Drag a Text node
2. Start typing: "Hello"
3. Keep typing: "Hello this is a very long text to test dynamic width"
4. Watch the node expand horizontally (max 500px)
```

#### Test 2: Dynamic Sizing (Height)
```
1. In Text node, press Enter multiple times
2. Type on different lines
3. Watch the textarea and node expand vertically
```

#### Test 3: Variable Detection - Single Variable
```
1. Clear the text field
2. Type: "Hello {{name}}"
3. ✅ Should see: 1 handle appear on left
4. ✅ Should see: Badge showing "1 var"
5. ✅ Should see: "name" listed in detected variables
```

#### Test 4: Variable Detection - Multiple Variables
```
1. Type: "{{greeting}} {{name}}, you are {{age}} years old and from {{city}}"
2. ✅ Should see: 4 handles on left (greeting, name, age, city)
3. ✅ Should see: Badge showing "4 vars"
4. ✅ Should see: All 4 variables listed with green badges
```

#### Test 5: Variable with Spaces
```
1. Type: "{{ input }}" (with spaces)
2. ✅ Should still detect "input" variable
```

#### Test 6: Duplicate Variables
```
1. Type: "{{name}} is {{name}}"
2. ✅ Should show only 1 handle (duplicates removed)
```

#### Test 7: Invalid Variables (Should NOT create handles)
```
1. Type: "{name}" (single braces)
2. Type: "{{name with spaces}}" (spaces in variable name)
3. Type: "{{123}}" (starts with number)
4. ✅ None of these should create handles
```

---

### Part 4: Backend Integration - Full Workflow

#### Test 1: Valid DAG (Simple Pipeline)
```
1. Drag: Input → LLM → Output
2. Connect them in sequence
3. Click "Submit Pipeline"
4. ✅ Alert should show:
   - Number of Nodes: 3
   - Number of Edges: 2
   - Is Valid DAG: ✓ Yes (green)
```

#### Test 2: Complex Valid DAG
```
1. Create this structure:
   Input1 ─┐
   Input2 ─┼─→ LLM ─→ Output
   Input3 ─┘
2. Click "Submit Pipeline"
3. ✅ Alert should show:
   - Number of Nodes: 5
   - Number of Edges: 4
   - Is Valid DAG: ✓ Yes
```

#### Test 3: Cycle Detection (Invalid DAG)
```
1. Create a cycle:
   A → B → C → A
2. Click "Submit Pipeline"
3. ✅ Alert should show:
   - Is Valid DAG: ✗ No (red)
   - Warning message about cycles
```

#### Test 4: No Nodes
```
1. Clear canvas (refresh if needed)
2. Click "Submit Pipeline"
3. ✅ Alert should show:
   - Number of Nodes: 0
   - Number of Edges: 0
   - Is Valid DAG: ✓ Yes (empty graph is valid DAG)
```

#### Test 5: Disconnected Components
```
1. Create two separate chains:
   A → B
   C → D
2. Click "Submit Pipeline"
3. ✅ Should work fine (disconnected components are still DAG)
```

#### Test 6: Backend Connection Error
```
1. Stop the backend server (Ctrl+C in backend terminal)
2. Click "Submit Pipeline"
3. ✅ Should show alert about backend connection
4. Restart backend and try again
```

---

## 🎬 Screen Recording Script

### Introduction (30 seconds)
"Hi, I'm Vandan. This is my solution for the VectorShift Frontend Assessment. 
I've completed all 4 parts: Node Abstraction, Styling, Text Node Logic, and Backend Integration.
Let me walk you through the features."

### Part 1 Demo (1 minute)
"First, the node abstraction. I created a BaseNode component that all nodes use.
Here are the original 4 nodes (drag each one).
And here are 5 new nodes I created (drag Filter, Transform, API, Conditional, Aggregator).
Notice they all have different configurations but share the same base component.
Let me show you the code briefly..." (Open BaseNode.js and nodeConfigs.js)

### Part 2 Demo (30 seconds)
"The styling is modern and cohesive. Notice the gradient toolbar, hover effects on nodes,
smooth animations, and the beautiful gradient submit button. Each node type has a unique color."

### Part 3 Demo (1 minute)
"The Text node has special logic. Watch as I type - it expands dynamically.
Now let me add variables: Hello {{name}}, you are {{age}} years old.
See how handles appear on the left for each variable? The node detects the pattern
and creates dynamic connections."

### Part 4 Demo (1 minute)
"Finally, backend integration. Let me create a simple pipeline and submit it.
The backend analyzes the graph structure and returns the results.
Notice the beautiful modal showing 3 nodes, 2 edges, and confirms it's a valid DAG.
Now let me create a cycle..." (Create A→B→C→A)
"Submit again - see, it detects the cycle and warns us."

### Code Walkthrough (1 minute)
"Let me briefly show the architecture:
- BaseNode: The core abstraction (show file)
- nodeConfigs: Simple config objects (show file)
- EnhancedTextNode: Dynamic sizing logic (show variable detection code)
- Backend: DAG validation with DFS (show Python code)
All organized, well-documented, and maintainable."

### Conclusion (15 seconds)
"That's my solution. Clean abstraction, modern design, working features, and solid backend integration.
Thank you for reviewing!"

**Total Time: ~4-5 minutes**

---

## 📊 Success Metrics

✅ **Code Quality**
- No duplicated code between nodes
- Clean separation of concerns
- Type-safe configurations
- Comprehensive comments

✅ **Functionality**
- All 9 nodes working
- Dynamic text node with variable detection
- Backend integration complete
- DAG validation accurate

✅ **Design**
- Modern, professional styling
- Smooth animations and transitions
- Consistent color scheme
- Responsive layout

✅ **Maintainability**
- New nodes can be created in <5 minutes
- Style changes apply globally
- Easy to extend and modify
- Well-documented code

---

## 🚀 Next Steps for Submission

1. **Record Screen**
   - Use tool like OBS, Loom, or Windows Game Bar
   - Follow the script above
   - Show functionality first, then code

2. **Create Zip File**
   ```powershell
   cd c:\projects
   Compress-Archive -Path vectorShift -DestinationPath Vandan_[LastName]_technical_assessment.zip
   ```

3. **Name Files**
   - Code: `Vandan_[LastName]_technical_assessment.zip`
   - Video: `Vandan_[LastName]_screenrecording.mp4`

4. **Submit via Form**
   - https://docs.google.com/forms/d/e/1FAIpQLSefic2bGl13U5Ka6aFuKZymYC71Urr8TTUobpZdKYKFnDTxkg/viewform

---

## 💡 Bonus Points to Mention

- **Extensibility**: New node types in <5 minutes
- **Performance**: React optimization with useCallback, useMemo
- **Error Handling**: Graceful backend error handling
- **Type Safety**: Pydantic models in backend
- **Algorithm**: Efficient O(V+E) DFS for cycle detection
- **UX**: Loading states, visual feedback, intuitive interactions
- **Code Organization**: Clear file structure and naming

---

Good luck with your submission! 🚀
