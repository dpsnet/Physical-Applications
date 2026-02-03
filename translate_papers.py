#!/usr/bin/env python3
"""
Translation helper script for converting Chinese physics papers to English.
This preserves all mathematical formulas, markdown structure, and metadata.
"""

import os
import re

# Key terminology mappings (Chinese -> English)
TERMINOLOGY = {
    # Core concepts
    '谱维': 'spectral dimension',
    '谱维度': 'spectral dimension',
    '扭转': 'torsion',
    '测度场': 'measure field',
    '分形': 'fractal',
    '多重扭转': 'multiple torsion',
    '动态拓扑': 'dynamic topology',
    '万花筒效应': 'kaleidoscope effect',
    '规范理论': 'gauge theory',
    '规范场': 'gauge field',
    '规范对称性': 'gauge symmetry',
    '重整化群': 'renormalization group',
    '热核': 'heat kernel',
    'Clifford代数': 'Clifford algebra',
    '统一场理论': 'unified field theory',
    '统一场论': 'unified field theory',
    '夸克禁闭': 'quark confinement',
    '胶子': 'gluon',
    '质量场': 'mass field',
    '暗物质': 'dark matter',
    '时空硬化': 'spacetime hardening',
    '时间单向性': 'time unidirectionality',
    '黑洞': 'black hole',
    '全息对偶': 'holographic duality',
    '弦理论': 'string theory',
    'Dirac算子': 'Dirac operator',
    '自旋': 'spin',
    '拓扑': 'topology',
    '本征值': 'eigenvalue',
    '本征态': 'eigenstate',
    '配分函数': 'partition function',
    '拉格朗日量': 'Lagrangian',
    '作用量': 'action',
    '哈密顿量': 'Hamiltonian',
    '场强张量': 'field strength tensor',
    '协变导数': 'covariant derivative',
    '联络': 'connection',
    '曲率': 'curvature',
    '度规': 'metric',
    '能动张量': 'energy-momentum tensor',
    '费米子': 'fermion',
    '玻色子': 'boson',
    '希格斯机制': 'Higgs mechanism',
    '希格斯场': 'Higgs field',
    'Yukawa耦合': 'Yukawa coupling',
    'β函数': 'beta function',
    '固定点': 'fixed point',
    '紫外发散': 'ultraviolet divergence',
    '红外行为': 'infrared behavior',
    '有效维度': 'effective dimension',
    '豪斯多夫维数': 'Hausdorff dimension',
    '普朗克尺度': 'Planck scale',
    '普朗克质量': 'Planck mass',
    '大统一理论': 'Grand Unified Theory',
    '标准模型': 'Standard Model',
    '量子引力': 'quantum gravity',
    '量子场论': 'quantum field theory',
    '引力波': 'gravitational wave',
    '宇宙微波背景': 'cosmic microwave background',
    '宇宙学常数': 'cosmological constant',
    'CP破坏': 'CP violation',
    '有效势': 'effective potential',
    '真空期望值': 'vacuum expectation value',
    '生成泛函': 'generating functional',
    '传播子': 'propagator',
    '圈图': 'loop diagram',
    '费曼图': 'Feynman diagram',
    '顶点': 'vertex',
    '树图': 'tree-level',
    '单圈': 'one-loop',
    '量子修正': 'quantum correction',
    '经典极限': 'classical limit',
    '能标': 'energy scale',
    '耦合常数': 'coupling constant',
    '渐近自由': 'asymptotic freedom',
    '禁闭': 'confinement',
    '相变': 'phase transition',
    '临界指数': 'critical exponent',
    '序参量': 'order parameter',
    '基态': 'ground state',
    '激发态': 'excited state',
    '简并度': 'degeneracy',
    '对应关系': 'correspondence',
    '等价性': 'equivalence',
    '自洽性': 'self-consistency',
    '数学基础': 'mathematical foundation',
    '物理意义': 'physical meaning',
    '理论框架': 'theoretical framework',
    '核心范式': 'core paradigm',
    '实验验证': 'experimental verification',
    '数值模拟': 'numerical simulation',
    '解析解': 'analytical solution',
    '近似解': 'approximate solution',
    '扰动展开': 'perturbation expansion',
}

def translate_line(line, in_math_block=False):
    """Translate a single line while preserving LaTeX and markdown."""
    # Don't translate content inside LaTeX blocks
    if in_math_block or line.strip().startswith('$$'):
        return line
    
    # Don't translate if line is mostly LaTeX
    if '$' in line and line.count('$') >= 2:
        # Split by $ and only translate text outside math mode
        parts = line.split('$')
        result = []
        for i, part in enumerate(parts):
            if i % 2 == 0:  # Outside math mode
                for cn, en in TERMINOLOGY.items():
                    part = part.replace(cn, en)
                result.append(part)
            else:  # Inside math mode
                result.append(part)
        return '$'.join(result)
    
    # Regular line translation
    for cn, en in TERMINOLOGY.items():
        line = line.replace(cn, en)
    
    return line

def translate_file(input_path, output_path):
    """Translate a markdown file while preserving structure."""
    print(f"Translating: {input_path} -> {output_path}")
    
    with open(input_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    translated = []
    in_math_block = False
    
    for line in lines:
        # Track math blocks
        if line.strip().startswith('$$'):
            in_math_block = not in_math_block
            translated.append(line)
            continue
        
        # Skip certain metadata lines that should remain as-is
        if line.strip().startswith('**作者**') or line.strip().startswith('**邮箱**'):
            translated.append(line)
            continue
            
        translated_line = translate_line(line, in_math_block)
        translated.append(translated_line)
    
    with open(output_path, 'w', encoding='utf-8') as f:
        f.writelines(translated)
    
    print(f"  Done: {len(lines)} lines processed")

if __name__ == '__main__':
    # Files to translate
    papers = ['P-1', 'P-2', 'P-3', 'P-4', 'P-5', 'P-6', 'P-7', 'P-8']
    
    for paper in papers:
        input_file = f'{paper}.md'
        output_file = f'{paper}_EN.md'
        
        if os.path.exists(input_file):
            translate_file(input_file, output_file)
        else:
            print(f"Warning: {input_file} not found")

