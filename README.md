# Gaohan Gao Academic Homepage

这是 Gaohan Gao（高晗）的个人学术主页项目，基于官方 [al-folio](https://github.com/alshedivat/al-folio) 最新 `main` 分支生成，并使用 al-folio v1.x 的 gem 化运行时。

网站定位为极简、白底、黑灰文字的学术主页，包含 About、Research、Publications、Projects 和 CV 五个页面。构建由 GitHub Actions 完成，生成的静态站点发布到 `gh-pages` 分支；不会使用 GitHub 默认的 Jekyll Pages 构建。

## 项目结构

项目保留了最新版 al-folio 正常构建所需的完整文件。最常修改的内容如下：

```text
.
├── _config.yml
├── Gemfile
├── _data
│   ├── cv.yml
│   └── socials.yml
├── _pages
│   ├── about.md
│   ├── research.md
│   ├── publications.md
│   ├── projects.md
│   └── cv.md
├── _projects
│   ├── 01-hsicd.md
│   ├── 02-sar-rgb-retrieval.md
│   └── 03-multi-agent-research-assistant.md
├── _bibliography
│   └── papers.bib
├── assets
│   ├── img
│   │   └── profile.jpg
│   └── pdf
│       └── CV.pdf
└── .github
    └── workflows
        └── deploy.yml
```

## 已配置的账号信息

### 1. GitHub 用户名

项目已配置为 GitHub 用户 `gaohan0121`，目标网址为 `https://gaohan0121.github.io`。不要删除 `_config.yml` 中的 `baseurl:`；用户主页的 `baseurl` 必须保持为空。

### 2. 邮箱

网站已使用简历中的邮箱 `gaohan050121@outlook.com`。如需更换，请同步修改：

- `_data/socials.yml`
- `_pages/about.md`
- `_data/cv.yml`
- `scripts/create_cv.py`，随后重新生成 PDF

### 3. 头像

当前 `assets/img/profile.jpg` 已替换为提供的证件照。首页通过以下配置将头像置于左侧并裁剪为圆形：

```yaml
profile:
  align: left
  image: profile.jpg
  image_circular: true
```

如要换图，直接用新的 JPG 覆盖 `assets/img/profile.jpg`，保持文件名不变即可。建议使用正方形或接近正方形的高清照片，并确保人物面部位于画面中央。

### 4. CV

`assets/pdf/CV.pdf` 是已根据当前公开信息生成的一页英文 Academic CV。若你已有正式 PDF，直接覆盖该文件即可，链接无需修改。

如需从脚本重新生成当前 PDF，请先安装 ReportLab，再运行：

```bash
python -m pip install reportlab
python scripts/create_cv.py
```

网页 CV 的结构化内容位于 `_data/cv.yml`，PDF 和网页 CV 是两个独立文件；更新一方不会自动更新另一方。

### 5. 论文作者、DOI 和链接

由于目前没有提供完整作者列表、DOI、论文链接和正式发表信息，`_bibliography/papers.bib` 使用了 `Gaohan Gao and others`，且未虚构 DOI、PDF 或项目链接。论文状态变化后，请补充真实字段。

## 推荐部署方式

### 方式 A：直接发布本项目

1. 登录 GitHub，新建公开仓库。
2. 仓库名称必须是：

   ```text
   gaohan0121.github.io
   ```

3. 不要初始化 README、License 或 `.gitignore`，创建一个空仓库。
4. 在本项目目录执行：

   ```bash
   git remote set-url origin https://github.com/gaohan0121/gaohan0121.github.io.git
   git add .
   git commit -m "Create academic homepage"
   git branch -M main
   git push -u origin main
   ```

   当前目录来自官方 al-folio 仓库，所以推送前必须先执行 `git remote set-url`，避免仍指向上游模板仓库。

### 方式 B：先使用官方高星模板，再复制定制文件

1. 打开 [alshedivat/al-folio](https://github.com/alshedivat/al-folio)。
2. 点击 `Use this template` -> `Create a new repository`。
3. 仓库名设为 `gaohan0121.github.io`。
4. 将本项目中的定制文件覆盖到新仓库。
5. 提交并推送到 `main` 分支。

方式 A 更快；方式 B 的优点是 GitHub 会把仓库标记为由官方模板创建。

## GitHub 设置

推送完成后进行以下设置：

1. 打开仓库 `Settings` -> `Actions` -> `General`。
2. 在 `Workflow permissions` 中选择 `Read and write permissions`，保存。
3. 打开 `Actions`，等待 `Deploy site` 工作流完成。
4. 工作流成功后会自动生成 `gh-pages` 分支。
5. 打开 `Settings` -> `Pages`。
6. `Source` 选择 `Deploy from a branch`。
7. 分支选择 `gh-pages`，目录选择 `/(root)`，保存。
8. 等待约一分钟，访问 `https://gaohan0121.github.io`。

请勿将 Pages 发布分支设为 `main`。`main` 保存 Jekyll 源代码，`gh-pages` 保存由 GitHub Actions 生成的静态网站。

## 自动部署原理

`.github/workflows/deploy.yml` 会在向 `main` 或 `master` 推送网页相关文件时执行：

1. 安装固定版本的 Ruby、Python 和 Node；
2. 使用 Bundler 安装 `Gemfile` 中的 Jekyll 与 al-folio v1.x gems；
3. 安装前端依赖和 ImageMagick；
4. 执行 `bundle exec jekyll build` 生成 `_site`；
5. 清理未使用的 CSS；
6. 将 `_site` 发布到 `gh-pages` 分支。

这就是为什么本项目不会依赖 GitHub 默认的受限 Jekyll 构建环境。

## 本地预览

al-folio 官方对 Windows 推荐使用 Docker。安装 Docker Desktop 后，在项目目录运行：

```bash
docker compose up
```

然后打开：

```text
http://localhost:8080
```

也可以安装 Ruby、Bundler、Node.js、Python、ImageMagick 后运行：

```bash
bundle install
npm ci
bundle exec jekyll serve
```

访问：

```text
http://localhost:4000
```

## 常见问题

### 页面没有样式或链接全部错误

确认用户主页配置为：

```yaml
url: https://gaohan0121.github.io
baseurl:
```

并确认 Pages 来源是 `gh-pages`，不是 `main`。

### Actions 报权限错误

到 `Settings` -> `Actions` -> `General`，将 Workflow permissions 改为 `Read and write permissions`。

### 修改后网站没有更新

打开 `Actions` -> `Deploy site` -> `Run workflow`，手动触发一次。浏览器端可强制刷新或清理缓存。

### 论文没有显示

检查 BibTeX 是否位于 `_bibliography/papers.bib`，并确保 BibTeX 语法完整。作者姓名应包含 `Gao, Gaohan`，以便 al-folio 正确高亮本人姓名。

## 内容维护

- 首页与简介：`_pages/about.md`
- 研究方向：`_pages/research.md`
- 论文数据：`_bibliography/papers.bib`
- 项目卡片：`_projects/*.md`
- 网页 CV：`_data/cv.yml`
- PDF CV：`assets/pdf/CV.pdf`
- 邮箱与 GitHub：`_data/socials.yml`
- 全站配置：`_config.yml`

## 隐私说明

本项目没有把简历中的手机号、出生日期、政治面貌、GPA、排名、课程分数、班级职务或奖学金信息放到公开网站。公开部署前，请再次检查 Git 历史和站点内容，确保没有提交不希望公开的信息。
