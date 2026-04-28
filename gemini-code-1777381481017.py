from weasyprint import HTML

# Conteúdo HTML detalhado para o plano do site "Veracidade"
html_content = """
<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <style>
        @page {
            size: A4;
            margin: 20mm;
            background-color: #f4f7f9;
        }
        body {
            font-family: 'Helvetica', 'Arial', sans-serif;
            color: #2c3e50;
            line-height: 1.6;
            margin: 0;
            padding: 0;
        }
        .header {
            background-color: #003366;
            color: white;
            padding: 30px;
            text-align: center;
            border-bottom: 5px solid #00509d;
        }
        .container {
            padding: 30px;
            background-color: white;
            margin: 0 10mm;
            box-shadow: 0 0 10px rgba(0,0,0,0.1);
        }
        h1 { margin: 0; font-size: 24pt; }
        h2 { color: #00509d; border-left: 5px solid #00509d; padding-left: 10px; margin-top: 30px; font-size: 16pt; }
        h3 { color: #34495e; font-size: 13pt; margin-top: 20px; }
        p { margin-bottom: 15px; }
        ul { margin-bottom: 15px; }
        table {
            width: 100%;
            border-collapse: collapse;
            margin: 20px 0;
        }
        th, td {
            border: 1px solid #dfe6e9;
            padding: 12px;
            text-align: left;
        }
        th {
            background-color: #f1f2f6;
            color: #2c3e50;
            font-weight: bold;
        }
        .code-block {
            background-color: #2d3436;
            color: #dfe6e9;
            padding: 15px;
            border-radius: 5px;
            font-family: 'Courier New', Courier, monospace;
            font-size: 9pt;
            white-space: pre-wrap;
        }
        .footer {
            text-align: center;
            font-size: 9pt;
            color: #7f8c8d;
            padding: 20px;
        }
        .highlight {
            color: #d63031;
            font-weight: bold;
        }
    </style>
</head>
<body>

<div class="header">
    <h1>Projeto Web: Veracidade</h1>
    <p>Plano de Implementação para Aprovação no Google AdSense</p>
</div>

<div class="container">
    <p>Este documento detalha a estrutura técnica e de conteúdo para o site <strong>Veracidade</strong>, de propriedade de <strong>Mateus Lourenço Bernardo</strong>, garantindo que todos os requisitos do Google AdSense sejam atendidos.</p>

    <h2>1. Requisitos de Domínio e Identidade</h2>
    <p>Para passar na auditoria do AdSense, o domínio deve ser profissional e de primeiro nível.</p>
    <ul>
        <li><strong>Sugestão de Domínio:</strong> <code>veracidade.com.br</code> ou <code>portalveracidade.com</code>.</li>
        <li><strong>Certificado SSL:</strong> O site DEVE carregar via HTTPS (Cadeado de segurança ativo).</li>
    </ul>

    <h2>2. Páginas de Conformidade (Obrigatórias)</h2>
    <table>
        <thead>
            <tr>
                <th>Página</th>
                <th>Finalidade para o AdSense</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td><strong>Política de Privacidade</strong></td>
                <td>Informa que o Google usa cookies para veicular anúncios. Fundamental para aprovação.</td>
            </tr>
            <tr>
                <td><strong>Termos de Uso</strong></td>
                <td>Define as regras de propriedade intelectual do site.</td>
            </tr>
            <tr>
                <td><strong>Sobre Nós</strong></td>
                <td>Humaniza o site. Deve mencionar Mateus Lourenço Bernardo como autoridade técnica.</td>
            </tr>
            <tr>
                <td><strong>Página de Contato</strong></td>
                <td>Prova que o site tem um administrador real e acessível.</td>
            </tr>
        </tbody>
    </table>

    <h2>3. Arquitetura de Conteúdo (E-E-A-T)</h2>
    <p>O Google prioriza conteúdo escrito por especialistas. O site será dividido em:</p>
    <ul>
        <li><strong>Manutenção Industrial:</strong> Guia técnico sobre bombas, redutores e compressores.</li>
        <li><strong>Mecânica de Precisão:</strong> Artigos sobre ajustes, tolerâncias e ferramentas.</li>
        <li><strong>Veracidade Industrial:</strong> Notícias e tendências reais do mercado de trabalho.</li>
    </ul>

    <h2>4. Estrutura de Código Otimizada</h2>
    <p>Estrutura limpa para garantir velocidade (Core Web Vitals):</p>
    <div class="code-block">
&lt;!DOCTYPE html&gt;
&lt;html lang="pt-br"&gt;
&lt;head&gt;
    &lt;meta charset="UTF-8"&gt;
    &lt;meta name="viewport" content="width=device-width, initial-scale=1.0"&gt;
    &lt;title&gt;Veracidade | Manutenção e Mecânica Industrial&lt;/title&gt;
    &lt;!-- Espaço para o Script do Google AdSense --&gt;
&lt;/head&gt;
&lt;body&gt;
    &lt;header&gt;
        &lt;h1&gt;Portal Veracidade&lt;/h1&gt;
    &lt;/header&gt;
    &lt;main&gt;
        &lt;article&gt;
            &lt;h2&gt;Técnicas de Manutenção Preditiva&lt;/h2&gt;
            &lt;p&gt;Conteúdo original de Mateus Lourenço Bernardo...&lt;/p&gt;
        &lt;/article&gt;
    &lt;/main&gt;
&lt;/body&gt;
&lt;/html&gt;
    </div>

    <h2>5. Checklist para Aprovação no AdSense</h2>
    <ul>
        <li><span class="highlight">Conteúdo Único:</span> Mínimo de 15 artigos com mais de 600 palavras cada.</li>
        <li><span class="highlight">Navegação Simples:</span> Menus claros e sem links quebrados.</li>
        <li><span class="highlight">Sem Plágio:</span> O Google rejeita sites que copiam notícias de outros portais.</li>
        <li><span class="highlight">Indexação:</span> O site deve estar cadastrado no Google Search Console.</li>
    </ul>
</div>

<div class="footer">
    Documento Gerado para Mateus Lourenço Bernardo &copy; 2026 - Projeto Veracidade
</div>

</body>
</html>
"""

# Gerar o PDF usando WeasyPrint
HTML(string=html_content).write_pdf("Blueprint_Site_Veracidade_AdSense.pdf")