# VectorShift Frontend Technical Assessment
## Solution by Vandan

This project implements a comprehensive pipeline builder with node abstraction, enhanced styling, dynamic text nodes, and backend integration.

---

## 🎯 Features Implemented

### Part 1: Node Abstraction ✅
- **BaseNode Component**: A flexible, reusable abstraction for all node types
- **Configuration-based Nodes**: Nodes defined through simple config objects
- **Zero Code Duplication**: All nodes share the same underlying component
- **5 New Nodes Created**:
  1. **Filter Node** - Filter data based on conditions
  2. **Transform Node** - Transform text (uppercase, lowercase, trim, reverse)
  3. **API Node** - Make HTTP API requests
  4. **Conditional Node** - Route based on conditional logic
  5. **Aggregator Node** - Combine multiple inputs

### Part 2: Styling ✅
- **Modern CSS Design System**: Custom CSS with CSS variables
- **Polished UI**: Professional gradient buttons, hover effects, shadows
- **Color-coded Nodes**: Each node type has a unique background color
- **Responsive Design**: Works on different screen sizes
- **Smooth Animations**: Transitions and hover effects throughout

### Part 3: Text Node Logic ✅
- **Dynamic Sizing**: Node width and height adjust based on text content
- **Variable Detection**: Automatically detects `{{variableName}}` patterns
- **Dynamic Handles**: Creates input handles on the left for each variable
- **Visual Feedback**: Shows detected variables with badges
- **Auto-expanding Textarea**: Grows with content

### Part 4: Backend Integration ✅
- **Frontend to Backend**: Submit button sends nodes and edges to backend
- **DAG Validation**: Backend checks if pipeline is a Directed Acyclic Graph
- **Custom Alert**: Beautiful modal displaying analysis results
- **Error Handling**: Graceful handling of connection issues
- **CORS Configured**: Backend properly configured for frontend requests

---

## 🚀 Setup Instructions

### Prerequisites
- Node.js (v14 or higher)
- Python 3.8 or higher
- pip

### Frontend Setup

```bash
# Navigate to frontend directory
cd c:\projects\vectorShift\frontend

# Install dependencies
npm install

# Install zustand (state management)
npm install zustand

# Start the development server
npm start
```

The frontend will open at `http://localhost:3000`

### Backend Setup

```bash
# Navigate to backend directory
cd c:\projects\vectorShift\backend

# Install Python dependencies
pip install fastapi uvicorn pydantic

# Start the backend server
uvicorn main:app --reload
```

The backend will run at `http://localhost:8000`

---

## 📁 Project Structure

```
vectorShift/
├── frontend/
│   ├── src/
│   │   ├── nodes/
│   │   │   ├── BaseNode.js           # Core abstraction component
│   │   │   ├── nodeConfigs.js        # Configuration for all nodes
│   │   │   ├── EnhancedTextNode.js   # Dynamic text node with variables
│   │   │   ├── inputNode.js          # Refactored input node
│   │   │   ├── outputNode.js         # Refactored output node
│   │   │   ├── llmNode.js            # Refactored LLM node
│   │   │   ├── textNode.js           # Refactored text node
│   │   │   ├── filterNode.js         # New filter node
│   │   │   ├── transformNode.js      # New transform node
│   │   │   ├── apiNode.js            # New API node
│   │   │   ├── conditionalNode.js    # New conditional node
│   │   │   └── aggregatorNode.js     # New aggregator node
│   │   ├── App.js                    # Main app component
│   │   ├── ui.js                     # ReactFlow canvas
│   │   ├── toolbar.js                # Node toolbar
│   │   ├── submit.js                 # Submit button with backend integration
│   │   ├── store.js                  # Zustand state management
│   │   ├── styles.css                # Comprehensive styling
│   │   └── ...
│   └── package.json
└── backend/
    └── main.py                       # FastAPI backend with DAG validation
```

---

## 🎨 Node Abstraction Architecture

### How It Works

The `BaseNode` component accepts a configuration object that defines:
- **Title**: Node display name
- **Description**: Optional description text
- **Fields**: Array of input fields (text, textarea, select, number, checkbox)
- **Handles**: Input/output connection points
- **Style**: Custom styling overrides
- **Dynamic Handles**: Support for variable-based connections

### Creating a New Node (Example)

```javascript
// 1. Define configuration in nodeConfigs.js
export const myNewNodeConfig = {
  title: 'My New Node',
  description: 'Does something cool',
  fields: [
    {
      name: 'myField',
      label: 'My Field',
      type: 'text',
      defaultValue: 'default value',
    }
  ],
  handles: {
    inputs: [{ id: 'input1' }],
    outputs: [{ id: 'output1' }]
  },
  style: {
    background: '#e0f2fe',
  }
};

// 2. Create node file (myNewNode.js)
import { createNodeFromConfig } from './BaseNode';
import { myNewNodeConfig } from './nodeConfigs';

export const MyNewNode = createNodeFromConfig(myNewNodeConfig);

// 3. Register in ui.js
import { MyNewNode } from './nodes/myNewNode';

const nodeTypes = {
  // ... existing nodes
  myNew: MyNewNode,
};

// 4. Add to toolbar.js
<DraggableNode type='myNew' label='My New' />
```

That's it! No need to write any JSX or handle state management.

---

## 🔧 Key Technical Features

### BaseNode Capabilities
- ✅ Multiple field types (text, textarea, select, number, checkbox)
- ✅ Dynamic handle positioning
- ✅ Variable extraction from text ({{variable}})
- ✅ Custom styling per node
- ✅ Automatic state management

### Text Node Features
- ✅ Auto-expanding textarea
- ✅ Dynamic width (220px - 500px)
- ✅ Variable detection with regex
- ✅ Visual variable badges
- ✅ Dynamic handle creation

### Backend Features
- ✅ DFS-based cycle detection
- ✅ DAG validation algorithm
- ✅ CORS configured for frontend
- ✅ Pydantic models for type safety
- ✅ Comprehensive error handling

---

## 🎯 Testing the Application

### Test Scenario 1: Basic Pipeline
1. Drag an **Input** node onto the canvas
2. Drag an **LLM** node
3. Drag an **Output** node
4. Connect: Input → LLM → Output
5. Click **Submit Pipeline**
6. Alert should show: 3 nodes, 2 edges, is_dag: true

### Test Scenario 2: Text Node with Variables
1. Drag a **Text** node onto the canvas
2. Type in the textarea: `Hello {{name}}, your age is {{age}}`
3. Observe: Two handles appear on the left (name, age)
4. Watch the node expand as you type more

### Test Scenario 3: Cycle Detection
1. Create nodes: A → B → C → A (creates a cycle)
2. Click **Submit Pipeline**
3. Alert should show: is_dag: false with warning message

### Test Scenario 4: New Nodes
1. Try all 5 new nodes: Filter, Transform, API, Conditional, Aggregator
2. Each has unique configurations and multiple handles
3. Create complex pipelines with branching logic

---

## 🎬 Screen Recording Checklist

When recording your demo, cover:
- [ ] Overview of the polished UI design
- [ ] Demonstrate node abstraction by showing multiple node types
- [ ] Create a Text node and show variable detection
- [ ] Show dynamic sizing of Text node
- [ ] Create a complete pipeline
- [ ] Submit and show the alert with results
- [ ] Create a pipeline with a cycle and show DAG validation
- [ ] Briefly explain the BaseNode architecture in code
- [ ] Show how easy it is to create new nodes (open nodeConfigs.js)

---

## 🏗️ Code Architecture Highlights

### Abstraction Benefits
- **90% less code** per node (from ~40 lines to ~4 lines)
- **Single source of truth** for node behavior
- **Easy maintenance** - style changes apply to all nodes
- **Rapid prototyping** - new nodes in minutes
- **Type safety** through configuration objects

### Styling Approach
- **CSS Variables** for consistent theming
- **Utility classes** for common patterns
- **Component-specific classes** for detailed styling
- **No inline styles** in components (except dynamic values)
- **Responsive design** with media queries

### Backend Design
- **Clean separation** of concerns
- **Efficient algorithm** - O(V+E) DFS for cycle detection
- **Type validation** with Pydantic
- **RESTful API** design
- **Extensible** for future features

---

## 📝 Notes for Reviewers

### Design Decisions
1. **BaseNode over HOC**: Chose render props pattern for clarity and flexibility
2. **Configuration Objects**: Easier to read and modify than JSX
3. **Enhanced TextNode**: Separate from BaseNode for specialized behavior
4. **CSS over styled-components**: Lighter weight, better performance
5. **DFS for DAG**: Standard, efficient algorithm with clear implementation

### Future Improvements
- Add undo/redo functionality
- Persist pipelines to backend
- Add node search/filter in toolbar
- Implement node validation rules
- Add keyboard shortcuts
- Export pipeline as JSON/image

---

## 🐛 Troubleshooting

### Frontend won't start
```bash
# Delete node_modules and reinstall
rm -rf node_modules
npm install
```

### Backend connection error
- Ensure backend is running on port 8000
- Check CORS configuration in main.py
- Verify fetch URL in submit.js

### Nodes not appearing
- Check browser console for errors
- Verify node is registered in ui.js nodeTypes
- Ensure toolbar includes the DraggableNode

---

## 📧 Contact

For any questions about this implementation:
- Email: recruiting@vectorshift.ai
- Assessment submission deadline: January 18, 2026, 11:59pm IST

---

**Built with ❤️ for the VectorShift Frontend Assessment**
