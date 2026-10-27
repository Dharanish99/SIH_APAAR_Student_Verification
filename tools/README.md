# Artifact tooling

These scripts package research and do not implement SetuTrace.

- `validate_research.py`: Python standard library; CSV/JSON, local Markdown targets, source-ID references and preserved-file hashes.
- `render_report.py`: ReportLab; renders docs/solution-report.md to output/pdf/solution-report.pdf with clickable references and contents. Uses Segoe UI on Windows or DejaVu Sans on Linux.
- `render_mind_map.py`: Pillow; maintains the twelve-branch hierarchy and generates Mermaid, SVG and PNG. The editable tldraw canvas uses the same hierarchy with a corrected manual layout.

Run from the repository root. Visual inspection is still required after a content or layout change. Rendered PDFs are not tagged accessible PDFs; the Markdown report and editable text sources remain available.
