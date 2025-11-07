# 📖 Poetry Analyzer

A professional desktop application for analyzing English poetry, detecting rhyme schemes, identifying poetic forms, and visualizing meter patterns. Built with Python and Tkinter.

![Python Version](https://img.shields.io/badge/python-3.7+-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)
![Platform](https://img.shields.io/badge/platform-Windows%20%7C%20macOS%20%7C%20Linux-lightgrey.svg)

## ✨ Features

### 🎯 Core Capabilities
- **Rhyme Scheme Detection**: Automatically identifies and labels rhyme patterns (ABAB, AABB, ABBA, etc.)
- **Poetic Form Recognition**: Detects classic forms including:
  - Shakespearean Sonnets
  - Petrarchan Sonnets
  - Haiku
  - Limericks
  - Quatrains (various types)
  - Couplets
  - Free Verse
- **Syllable Counting**: Accurate syllable analysis for each line
- **Meter Detection**: Identifies whether the poem follows a consistent metrical pattern
- **Visual Analysis**: Color-coded rhyme scheme visualization with detailed breakdowns

### 🎨 User Interface
- Clean, professional GUI with a literary aesthetic
- Split-panel design: input on the left, analysis on the right
- Syntax highlighting for different rhyme patterns
- Real-time analysis with visual feedback
- Sample poem loader for quick testing

## 📋 Requirements

- Python 3.7 or higher
- Tkinter (usually comes pre-installed with Python)

### Checking Your Installation

```bash
python --version  # Should show 3.7 or higher
python -m tkinter  # Should open a small Tk window
```

## 🚀 Installation

### Option 1: Clone the Repository

```bash
git clone https://github.com/yourusername/poetry-analyzer.git
cd poetry-analyzer
python poetry.py
```

### Option 2: Direct Download

1. Download `poetry.py` from this repository
2. Navigate to the download location
3. Run the application:

```bash
python poetry.py
```

No additional dependencies required! 🎉

## 💻 Usage

### Quick Start

1. **Launch the application**:
   ```bash
   python poetry.py
   ```

2. **Load a sample poem**: Click the "Load Sample" button to see a Shakespearean example

3. **Analyze your own poem**:
   - Type or paste your poem into the left panel
   - Each line should be on a new line
   - Click "🔍 Analyze Poem"

4. **Review the analysis**: The right panel will display:
   - Detected poetic form
   - Rhyme scheme with color-coded labels
   - Syllable counts per line with visual bars
   - Meter consistency analysis
   - Overall statistics

### Example Input

```
Shall I compare thee to a summer's day?
Thou art more lovely and more temperate:
Rough winds do shake the darling buds of May,
And summer's lease hath all too short a date
```

### Example Output

```
Detected Poetic Form
➜ Shakespearean Sonnet (partial)

Rhyme Scheme Analysis
Pattern: ABAB

A  Shall I compare thee to a summer's day?
   ↳ Rhyme: day

B  Thou art more lovely and more temperate:
   ↳ Rhyme: temperate

A  Rough winds do shake the darling buds of May,
   ↳ Rhyme: May

B  And summer's lease hath all too short a date
   ↳ Rhyme: date
```

## 🔧 How It Works

### Rhyme Detection Algorithm

The analyzer uses phonetic approximation to detect rhymes:

1. **Extract last word** from each line
2. **Identify phonetic ending**: Finds the last vowel cluster and all following sounds
3. **Compare endings**: Matches words with similar phonetic patterns
4. **Classify rhyme type**:
   - Perfect rhyme: Identical endings (day/May)
   - Near rhyme: Similar but not identical endings

### Syllable Counting

Uses a rule-based approach:
- Counts vowel clusters as syllable units
- Accounts for silent 'e' at word endings
- Handles common English pronunciation patterns

### Form Detection

Pattern matching against known poetic structures:
- **Sonnets**: 14 lines with specific rhyme schemes
- **Haiku**: 5-7-5 syllable pattern
- **Limerick**: 5 lines with AABBA scheme
- **Quatrains**: 4-line stanzas with various patterns

## 📊 Supported Poetic Forms

| Form | Lines | Rhyme Scheme | Example |
|------|-------|--------------|---------|
| Shakespearean Sonnet | 14 | ABABCDCDEFEFGG | Shakespeare's sonnets |
| Petrarchan Sonnet | 14 | ABBAABBACDECDE | Italian sonnets |
| Haiku | 3 | N/A (5-7-5 syllables) | Japanese verse |
| Limerick | 5 | AABBA | Humorous verse |
| Alternate Rhyme | 4 | ABAB | Common quatrain |
| Couplet | 2+ | AABB | Heroic couplets |

## 🌍 Roadmap

### Upcoming Features
- [ ] Multi-language support (Hindi, Spanish, French, Arabic, Urdu)
- [ ] Export analysis to PDF/Text
- [ ] Stress pattern visualization
- [ ] Dictionary integration for word meanings
- [ ] Historical poet comparison mode
- [ ] Save/Load poem collections
- [ ] Dark mode theme

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

1. **Fork the repository**
2. **Create a feature branch**: `git checkout -b feature/amazing-feature`
3. **Commit your changes**: `git commit -m 'Add amazing feature'`
4. **Push to the branch**: `git push origin feature/amazing-feature`
5. **Open a Pull Request**

### Areas for Contribution
- Improved rhyme detection algorithms
- Additional language support
- New poetic form detection
- UI/UX enhancements
- Documentation improvements

## 🐛 Bug Reports

Found a bug? Please open an issue with:
- Python version
- Operating system
- Steps to reproduce
- Expected vs actual behavior
- Sample poem that caused the issue (if applicable)

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👨‍💻 Author

Created with ❤️ for poetry enthusiasts and literary analysts

## 🙏 Acknowledgments

- Inspired by classical poetry analysis techniques
- Built with Python's Tkinter for cross-platform compatibility
- Rhyme detection based on phonetic approximation algorithms

## 📚 Resources

- [Poetry Foundation](https://www.poetryfoundation.org/) - Poetry examples and education
- [Python Tkinter Documentation](https://docs.python.org/3/library/tkinter.html)
- [Poetic Forms Guide](https://www.poetryarchive.org/glossary) - Understanding different forms

---

**Star ⭐ this repository if you find it useful!**

For questions or suggestions, please open an issue or contact the maintainer.
