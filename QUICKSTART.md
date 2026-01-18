# 🚀 Quick Start Guide

## Prerequisites
- Node.js v14+
- Python 3.8+
- npm and pip installed

## Installation & Setup (First Time)

### Frontend
```powershell
cd c:\projects\vectorShift\frontend
npm install
```

### Backend
```powershell
cd c:\projects\vectorShift\backend
pip install fastapi uvicorn pydantic
```

## Running the Application

### Terminal 1 - Frontend
```powershell
cd c:\projects\vectorShift\frontend
npm start
```
Opens at: http://localhost:3000

### Terminal 2 - Backend
```powershell
cd c:\projects\vectorShift\backend
python -m uvicorn main:app --reload
```
Runs at: http://localhost:8000

## Testing the App

1. **Open browser**: Navigate to http://localhost:3000
2. **Drag nodes**: Drag nodes from toolbar onto canvas
3. **Connect nodes**: Click and drag from one handle to another
4. **Configure nodes**: Edit fields within each node
5. **Test Text Node**: Type `Hello {{name}}` to see dynamic handles
6. **Submit**: Click "Submit Pipeline" to see DAG analysis

## Quick Feature Tests

### Test Node Abstraction
- Drag all 9 nodes onto canvas
- Notice they all work seamlessly

### Test Styling
- Hover over nodes (lift effect)
- Connect nodes (smooth animated edges)
- Click Submit button (gradient, hover effect)

### Test Text Node
- Type: `{{name}} is {{age}} years old`
- See 2 handles appear on left
- Watch node expand as you type

### Test Backend Integration
- Create: Input → LLM → Output
- Click Submit
- See alert with: 3 nodes, 2 edges, DAG: Yes

### Test Cycle Detection
- Create: A → B → C → A
- Click Submit
- See alert with: DAG: No + warning

## Troubleshooting

### Frontend won't start
```powershell
cd c:\projects\vectorShift\frontend
rm -rf node_modules
npm install
npm start
```

### Backend won't start
```powershell
cd c:\projects\vectorShift\backend
pip install --upgrade fastapi uvicorn pydantic
python -m uvicorn main:app --reload
```

### CORS errors
- Make sure backend is running on port 8000
- Check CORS configuration in backend/main.py
- Frontend should be on port 3000

### Nodes not appearing
- Check browser console (F12)
- Verify node is registered in src/ui.js
- Check toolbar has DraggableNode component

## Project Structure

```
vectorShift/
├── frontend/
│   ├── src/
│   │   ├── nodes/          # All node components
│   │   ├── App.js          # Main component
│   │   ├── ui.js           # ReactFlow canvas
│   │   ├── toolbar.js      # Node toolbar
│   │   ├── submit.js       # Submit with backend
│   │   └── styles.css      # All styling
│   └── package.json
├── backend/
│   └── main.py            # FastAPI with DAG validation
├── README.md              # Full documentation
├── TESTING_GUIDE.md       # Detailed test scenarios
└── COMPLETION_SUMMARY.md  # Implementation summary
```

## Key Files to Review

1. **nodes/BaseNode.js** - The magic abstraction
2. **nodes/nodeConfigs.js** - How easy it is to add nodes
3. **nodes/EnhancedTextNode.js** - Dynamic text logic
4. **styles.css** - Complete design system
5. **backend/main.py** - DAG validation algorithm

## Adding a New Node (5 minutes)

1. Add config to `nodes/nodeConfigs.js`:
```javascript
export const myNodeConfig = {
  title: 'My Node',
  fields: [
    { name: 'field1', label: 'Field 1', type: 'text' }
  ],
  handles: {
    inputs: [{ id: 'in' }],
    outputs: [{ id: 'out' }]
  }
};
```

2. Create `nodes/myNode.js`:
```javascript
import { createNodeFromConfig } from './BaseNode';
import { myNodeConfig } from './nodeConfigs';
export const MyNode = createNodeFromConfig(myNodeConfig);
```

3. Register in `ui.js`:
```javascript
import { MyNode } from './nodes/myNode';
const nodeTypes = { ...existing, myNode: MyNode };
```

4. Add to `toolbar.js`:
```javascript
<DraggableNode type='myNode' label='My Node' />
```

Done! 🎉

## Documentation

- **README.md** - Complete project overview and architecture
- **TESTING_GUIDE.md** - Step-by-step testing instructions
- **COMPLETION_SUMMARY.md** - Implementation details and metrics

## Screen Recording Tips

1. Close unnecessary applications
2. Use 1920x1080 resolution if possible
3. Test audio before recording
4. Follow the script in TESTING_GUIDE.md
5. Show both functionality AND code
6. Keep it under 5-6 minutes
7. Be enthusiastic and confident!

## Submission

1. **Create zip**:
```powershell
cd c:\projects
Compress-Archive -Path vectorShift -DestinationPath Vandan_[LastName]_technical_assessment.zip
```

2. **Name video**:
`Vandan_[LastName]_screenrecording.mp4`

3. **Submit**:
https://docs.google.com/forms/d/e/1FAIpQLSefic2bGl13U5Ka6aFuKZymYC71Urr8TTUobpZdKYKFnDTxkg/viewform

**Deadline**: January 18, 2026, 11:59pm IST

---

Good luck! 🚀
