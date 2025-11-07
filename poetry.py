import tkinter as tk
from tkinter import ttk, scrolledtext, messagebox
import re

class PoetryAnalyzer:
    def __init__(self, root):
        self.root = root
        self.root.title("Poetry Analyzer - English Rhyme Scheme Detector")
        self.root.geometry("1200x700")
        self.root.configure(bg="#FFF8F0")
        
        # Configure style
        style = ttk.Style()
        style.theme_use('clam')
        
        # Main container
        main_frame = tk.Frame(root, bg="#FFF8F0")
        main_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
        
        # Title
        title_frame = tk.Frame(main_frame, bg="#FFF8F0")
        title_frame.pack(fill=tk.X, pady=(0, 20))
        
        title_label = tk.Label(
            title_frame, 
            text="📖 Poetry Analyzer", 
            font=("Georgia", 28, "bold"),
            bg="#FFF8F0",
            fg="#8B4513"
        )
        title_label.pack()
        
        subtitle = tk.Label(
            title_frame,
            text="Discover the hidden structure in verse",
            font=("Georgia", 12, "italic"),
            bg="#FFF8F0",
            fg="#666"
        )
        subtitle.pack()
        
        # Content frame (two columns)
        content_frame = tk.Frame(main_frame, bg="#FFF8F0")
        content_frame.pack(fill=tk.BOTH, expand=True)
        
        # Left panel - Input
        left_panel = tk.Frame(content_frame, bg="white", relief=tk.RAISED, bd=2)
        left_panel.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=(0, 10))
        
        # Input header
        input_header = tk.Frame(left_panel, bg="white")
        input_header.pack(fill=tk.X, padx=10, pady=10)
        
        tk.Label(
            input_header,
            text="Enter Your Poem",
            font=("Georgia", 16, "bold"),
            bg="white",
            fg="#333"
        ).pack(side=tk.LEFT)
        
        sample_btn = tk.Button(
            input_header,
            text="Load Sample",
            command=self.load_sample,
            bg="#FFE4B5",
            fg="#8B4513",
            font=("Arial", 10),
            relief=tk.FLAT,
            padx=15,
            pady=5,
            cursor="hand2"
        )
        sample_btn.pack(side=tk.RIGHT)
        
        # Text input
        self.poem_input = scrolledtext.ScrolledText(
            left_panel,
            font=("Georgia", 12),
            wrap=tk.WORD,
            bg="#FFFEF8",
            fg="#333",
            relief=tk.FLAT,
            padx=10,
            pady=10
        )
        self.poem_input.pack(fill=tk.BOTH, expand=True, padx=10, pady=(0, 10))
        
        # Analyze button
        analyze_btn = tk.Button(
            left_panel,
            text="🔍 Analyze Poem",
            command=self.analyze_poem,
            bg="#D2691E",
            fg="white",
            font=("Arial", 12, "bold"),
            relief=tk.FLAT,
            padx=20,
            pady=10,
            cursor="hand2"
        )
        analyze_btn.pack(pady=(0, 10))
        
        # Right panel - Analysis
        right_panel = tk.Frame(content_frame, bg="white", relief=tk.RAISED, bd=2)
        right_panel.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)
        
        # Analysis header
        analysis_header = tk.Frame(right_panel, bg="white")
        analysis_header.pack(fill=tk.X, padx=10, pady=10)
        
        tk.Label(
            analysis_header,
            text="✨ Analysis Results",
            font=("Georgia", 16, "bold"),
            bg="white",
            fg="#333"
        ).pack(side=tk.LEFT)
        
        # Analysis output (scrollable)
        self.analysis_output = scrolledtext.ScrolledText(
            right_panel,
            font=("Arial", 11),
            wrap=tk.WORD,
            bg="#FFF5EE",
            fg="#333",
            relief=tk.FLAT,
            padx=15,
            pady=15,
            state=tk.DISABLED
        )
        self.analysis_output.pack(fill=tk.BOTH, expand=True, padx=10, pady=(0, 10))
        
        # Configure tags for colored output
        self.analysis_output.tag_config("title", font=("Georgia", 14, "bold"), foreground="#8B4513")
        self.analysis_output.tag_config("heading", font=("Arial", 12, "bold"), foreground="#D2691E")
        self.analysis_output.tag_config("rhyme_a", background="#FFE4E1", foreground="#8B0000")
        self.analysis_output.tag_config("rhyme_b", background="#E0F0FF", foreground="#00008B")
        self.analysis_output.tag_config("rhyme_c", background="#E0FFE0", foreground="#006400")
        self.analysis_output.tag_config("rhyme_d", background="#FFF0E0", foreground="#8B4500")
        self.analysis_output.tag_config("rhyme_e", background="#F0E0FF", foreground="#4B0082")
        self.analysis_output.tag_config("rhyme_f", background="#FFE0F0", foreground="#8B008B")
        self.analysis_output.tag_config("rhyme_g", background="#E0FFFF", foreground="#008B8B")
        self.analysis_output.tag_config("rhyme_h", background="#FFFFE0", foreground="#8B8B00")
        self.analysis_output.tag_config("line", font=("Georgia", 11), foreground="#333")
        self.analysis_output.tag_config("stat", font=("Arial", 11), foreground="#666")
        
        # Initial message
        self.show_initial_message()
    
    def show_initial_message(self):
        self.analysis_output.config(state=tk.NORMAL)
        self.analysis_output.delete(1.0, tk.END)
        self.analysis_output.insert(tk.END, "\n\n\n")
        self.analysis_output.insert(tk.END, "        📖\n\n", "title")
        self.analysis_output.insert(tk.END, "    Enter a poem to see its analysis\n\n", "heading")
        self.analysis_output.insert(tk.END, "    The analyzer will detect:\n", "stat")
        self.analysis_output.insert(tk.END, "    • Rhyme schemes (ABAB, AABB, etc.)\n", "stat")
        self.analysis_output.insert(tk.END, "    • Poetic forms (Sonnet, Haiku, etc.)\n", "stat")
        self.analysis_output.insert(tk.END, "    • Syllable counts and meter\n", "stat")
        self.analysis_output.config(state=tk.DISABLED)
    
    def load_sample(self):
        sample = """Shall I compare thee to a summer's day?
Thou art more lovely and more temperate:
Rough winds do shake the darling buds of May,
And summer's lease hath all too short a date"""
        self.poem_input.delete(1.0, tk.END)
        self.poem_input.insert(1.0, sample)
        self.analyze_poem()
    
    def get_phonetic_ending(self, word):
        """Get phonetic ending for rhyme detection"""
        w = word.lower()
        w = re.sub(r'[^a-z]', '', w)
        vowels = 'aeiouy'
        
        # Find last vowel
        last_vowel_idx = -1
        for i in range(len(w) - 1, -1, -1):
            if w[i] in vowels:
                last_vowel_idx = i
                break
        
        if last_vowel_idx == -1:
            return w[-3:] if len(w) >= 3 else w
        
        # Get ending from last vowel
        ending = w[last_vowel_idx:]
        
        # Include preceding consonant
        if last_vowel_idx > 0:
            ending = w[last_vowel_idx - 1] + ending
        
        return ending
    
    def check_rhyme(self, word1, word2):
        """Check if two words rhyme"""
        if not word1 or not word2:
            return False
        
        ending1 = self.get_phonetic_ending(word1)
        ending2 = self.get_phonetic_ending(word2)
        
        # Perfect rhyme
        if ending1 == ending2 and len(ending1) >= 2:
            return True
        
        # Near rhyme
        if len(ending1) >= 2 and len(ending2) >= 2:
            min_len = min(len(ending1), len(ending2))
            if ending1[-min_len:] == ending2[-min_len:]:
                return True
        
        return False
    
    def count_syllables(self, word):
        """Count syllables in a word (approximation)"""
        word = word.lower()
        word = re.sub(r'[^a-z]', '', word)
        
        if len(word) <= 3:
            return 1
        
        vowels = 'aeiouy'
        count = 0
        prev_was_vowel = False
        
        for char in word:
            is_vowel = char in vowels
            if is_vowel and not prev_was_vowel:
                count += 1
            prev_was_vowel = is_vowel
        
        # Silent e
        if word.endswith('e'):
            count -= 1
        
        return max(1, count)
    
    def detect_form(self, lines, rhyme_scheme, syllable_counts):
        """Detect poetic form"""
        scheme_str = ''.join(rhyme_scheme)
        num_lines = len(lines)
        
        # Sonnet detection
        if num_lines == 14:
            if scheme_str == 'ABABCDCDEFEFGG':
                return 'Shakespearean Sonnet'
            elif re.match(r'ABBAABBA(CDECDE|CDCDCD)', scheme_str):
                return 'Petrarchan Sonnet'
            else:
                return 'Sonnet (variant)'
        
        # Haiku
        if num_lines == 3 and syllable_counts == [5, 7, 5]:
            return 'Haiku'
        
        # Limerick
        if num_lines == 5 and scheme_str == 'AABBA':
            return 'Limerick'
        
        # Couplets
        if all(s in ['A', 'B'] for s in rhyme_scheme) and num_lines % 2 == 0:
            return 'Couplets'
        
        # Quatrain
        if num_lines == 4:
            if scheme_str == 'ABAB':
                return 'Alternate Rhyme Quatrain'
            elif scheme_str == 'AABB':
                return 'Couplet Quatrain'
            elif scheme_str == 'ABBA':
                return 'Enclosed Rhyme Quatrain'
        
        return 'Free Verse'
    
    def analyze_poem(self):
        """Analyze the poem and display results"""
        poem_text = self.poem_input.get(1.0, tk.END).strip()
        
        if not poem_text:
            messagebox.showwarning("Empty Input", "Please enter a poem to analyze!")
            return
        
        lines = [line.strip() for line in poem_text.split('\n') if line.strip()]
        
        if len(lines) == 0:
            messagebox.showwarning("Invalid Input", "Please enter valid poem lines!")
            return
        
        # Extract last words
        last_words = []
        for line in lines:
            words = line.split()
            if words:
                last_word = re.sub(r'[.,!?;:"\']', '', words[-1])
                last_words.append(last_word)
            else:
                last_words.append('')
        
        # Detect rhyme scheme
        rhyme_scheme = []
        current_letter = ord('A')
        
        for i, word in enumerate(last_words):
            found_rhyme = False
            
            for j in range(i):
                if self.check_rhyme(word, last_words[j]):
                    rhyme_scheme.append(rhyme_scheme[j])
                    found_rhyme = True
                    break
            
            if not found_rhyme:
                rhyme_scheme.append(chr(current_letter))
                current_letter += 1
        
        # Count syllables
        syllable_counts = []
        for line in lines:
            words = line.split()
            total = sum(self.count_syllables(re.sub(r'[^a-zA-Z]', '', w)) for w in words)
            syllable_counts.append(total)
        
        # Detect meter
        avg_syllables = sum(syllable_counts) / len(syllable_counts)
        is_metered = all(abs(c - avg_syllables) <= 2 for c in syllable_counts)
        
        # Detect form
        form = self.detect_form(lines, rhyme_scheme, syllable_counts)
        
        # Display results
        self.display_analysis(lines, rhyme_scheme, last_words, syllable_counts, 
                            is_metered, int(avg_syllables), form)
    
    def display_analysis(self, lines, rhyme_scheme, last_words, syllable_counts, 
                        is_metered, avg_syllables, form):
        """Display analysis results with formatting"""
        self.analysis_output.config(state=tk.NORMAL)
        self.analysis_output.delete(1.0, tk.END)
        
        # Detected Form
        self.analysis_output.insert(tk.END, "Detected Poetic Form\n", "title")
        self.analysis_output.insert(tk.END, f"➜ {form}\n\n", "heading")
        
        # Rhyme Scheme Visualization
        self.analysis_output.insert(tk.END, "Rhyme Scheme Analysis\n", "title")
        self.analysis_output.insert(tk.END, f"Pattern: {''.join(rhyme_scheme)}\n\n", "heading")
        
        for i, line in enumerate(lines):
            letter = rhyme_scheme[i]
            tag = f"rhyme_{letter.lower()}"
            
            self.analysis_output.insert(tk.END, f" {letter} ", tag)
            self.analysis_output.insert(tk.END, f"  {line}\n", "line")
            self.analysis_output.insert(tk.END, f"      ↳ Rhyme: {last_words[i]}\n", "stat")
        
        # Syllable & Meter Analysis
        self.analysis_output.insert(tk.END, "\n\nMeter & Syllable Analysis\n", "title")
        
        for i, count in enumerate(syllable_counts):
            bar = "█" * count
            self.analysis_output.insert(tk.END, f"Line {i+1}: ", "heading")
            self.analysis_output.insert(tk.END, f"{bar} ({count} syllables)\n", "stat")
        
        self.analysis_output.insert(tk.END, f"\nAverage: {avg_syllables} syllables per line\n", "stat")
        meter_status = "Yes (consistent meter)" if is_metered else "No (free verse)"
        self.analysis_output.insert(tk.END, f"Metered: {meter_status}\n", "stat")
        
        # Statistics
        self.analysis_output.insert(tk.END, "\n\nPoem Statistics\n", "title")
        self.analysis_output.insert(tk.END, f"Total Lines: {len(lines)}\n", "stat")
        self.analysis_output.insert(tk.END, f"Unique Rhymes: {len(set(rhyme_scheme))}\n", "stat")
        self.analysis_output.insert(tk.END, f"Total Syllables: {sum(syllable_counts)}\n", "stat")
        
        self.analysis_output.config(state=tk.DISABLED)

if __name__ == "__main__":
    root = tk.Tk()
    app = PoetryAnalyzer(root)
    root.mainloop()