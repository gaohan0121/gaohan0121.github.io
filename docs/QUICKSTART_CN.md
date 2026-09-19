# 快速开始指南

本指南用于在几分钟内快速启动一个可用的 al-folio 网站，不涉及复杂的深度定制。

> 视频教程：可以观看原项目提供的操作视频 `assets/video/tutorial_al_folio.mp4`。

## 第一步：创建仓库

> 官方通用流程建议使用 **Use this template**，而不是 Fork。这样创建出来的网站仓库与 al-folio 上游仓库相互独立，不会误把个人网站修改提交到官方项目。

通用操作如下：

1. 打开 [al-folio 官方仓库](https://github.com/alshedivat/al-folio)。
2. 点击页面右上角绿色的 **Use this template**。
3. 选择 **Create a new repository**。
4. 根据网站类型设置仓库名称：
   - 如果希望网站地址是 `username.github.io`，仓库必须命名为 `username.github.io`。
   - 如果希望网站地址是 `username.github.io/project-name`，可以使用其他仓库名，例如 `my-research-website`。
5. 点击 **Create repository from template**。

如果误用了 Fork，也仍然可以部署，但修改时必须确认自己操作的是个人仓库，而不是向 al-folio 官方仓库提交 Pull Request。

### 本项目应采用的操作

Gaohan Gao 的网站已经在本地基于官方模板完成，因此不要再次使用模板创建，直接创建一个空仓库即可：

- 仓库名：`gaohan0121.github.io`
- 可见性：`Public`
- 不要勾选创建 README、`.gitignore` 或 License

## 第二步：配置自动部署权限

1. 进入新仓库。
2. 点击 **Settings**。
3. 在左侧点击 **Actions**，然后选择 **General**。
4. 找到页面下方的 **Workflow permissions**。
5. 选择 **Read and write permissions**。
6. 点击 **Save**。

此权限允许 al-folio 的 GitHub Actions 工作流把生成的网站写入 `gh-pages` 分支。

## 第三步：填写个人信息

官方模板要求修改 `_config.yml` 中的以下字段：

```yaml
title: My Website
first_name: Your
last_name: Name
url: https://your-username.github.io
baseurl:
```

其中：

- `url` 应替换为真实的网站地址；
- 用户主页的 `baseurl` 必须留空；
- 不要删除 `baseurl:` 这一行。

当前项目已经配置为：

```yaml
title: Gaohan Gao
first_name: Gaohan
last_name: Gao
url: https://gaohan0121.github.io
baseurl:
```

因此无需再次修改这些字段。

## 第四步：查看网站

1. 打开仓库的 **Actions** 标签页。
2. 等待名为 **Deploy site** 的工作流完成，通常需要几分钟。
3. 成功时会显示绿色对勾，并生成 `gh-pages` 分支。
4. 进入 **Settings** -> **Pages** -> **Build and deployment**。
5. 将 **Source** 设置为 **Deploy from a branch**。
6. 将分支设置为 **gh-pages**，不要选择 `main`。
7. 目录选择 `/(root)`，点击 **Save**。
8. 等待 GitHub 的 `pages-build-deployment` 完成。
9. 访问 <https://gaohan0121.github.io>。

## 后续内容维护

### 修改个人内容

- 头像：`assets/img/profile.jpg`
- 首页简介：`_pages/about.md`
- 研究方向：`_pages/research.md`
- 论文：`_bibliography/papers.bib`
- 项目：`_projects/*.md`
- 网页版 CV：`_data/cv.yml`
- PDF CV：`assets/pdf/CV.pdf`
- 社交链接：`_data/socials.yml`

### 修改外观

- 返回顶部按钮：`_config.yml` 中的 `back_to_top`
- 固定导航栏：`navbar_fixed`
- 固定页脚：`footer_fixed`
- 页面最大宽度：`max_width`
- 功能开关：`enabled: true/false` 和 `enable_*`

al-folio v1.x 的主题颜色由 `al_folio_core` gem 中的 Sass tokens 管理，不是简单的 `_config.yml` 字段。本项目保持官方默认的极简白色学术风格，无需修改主题运行时代码。

## 本项目的最短发布流程

在 GitHub 创建空的 `gaohan0121.github.io` 仓库后，打开 PowerShell，执行：

```powershell
cd "D:\CodexHome\visualizations\2026\09\19\01a0b7be-9f31-77f2-a2fe-9b89c2a8fff2\gaohan-academic-homepage"
git push -u origin main
```

然后完成：

1. `Settings` -> `Actions` -> `General` -> `Read and write permissions`。
2. `Actions` -> `Deploy site`，等待绿色对勾。
3. `Settings` -> `Pages` -> `Deploy from a branch`。
4. 选择 `gh-pages` 和 `/(root)`。
5. 打开 <https://gaohan0121.github.io>。

## 常见错误

### `git push` 提示 Repository not found

确认：

- GitHub 已经创建 `gaohan0121.github.io`；
- 当前登录账号是 `gaohan0121`；
- 仓库地址为 `https://github.com/gaohan0121/gaohan0121.github.io`。

### Actions 提示权限不足

进入 `Settings` -> `Actions` -> `General`，选择 `Read and write permissions`，保存后重新运行工作流。

### 没有 `gh-pages` 分支

只有 `Deploy site` 成功后才会生成该分支。先检查 Actions 日志，不要把 Pages 发布源设置成 `main`。

### 网站没有样式或链接错误

确认 `_config.yml` 是：

```yaml
url: https://gaohan0121.github.io
baseurl:
```

并确认 Pages 发布分支是 `gh-pages`。
