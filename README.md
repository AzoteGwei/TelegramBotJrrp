# TelegramBotJrrp

这个东西只有一个作用 ———— 今日人品。

## 直接运行

### 依赖

```bash
pip install pyTelegramBotAPI aiohttp
```

### 运行

```bash
python3 main.py <Your Token Here>
```

## 使用 Docker

### 拉取

```bash
docker pull ghcr.io/cat0x1f/telegrambotjrrp:latest
```

### Docker 运行

```bash
docker run --env BOTTOKEN=yourtoken ghcr.io/cat0x1f/telegrambotjrrp:latest
```

其中的 `yourtoken` 为从 @BotFather 获取的令牌。
