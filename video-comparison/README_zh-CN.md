# 更多视频模型：同提示词案例与消费

2026-10-20.

| 模型 | 请求 | 实际时长 | API确认消费 | 本例美元/秒 | 当前档位价格 |
|---|---|---:|---:|---:|---|
| kling-3.0-turbo | 4s / 720p | 4.04s | $0.32 | $0.079208/s | $0.08/s |
| MiniMax-H3 | 5s / 768p | 5.17s | $0.32 | $0.061896/s | $0.064/s |
| seedance-2-5 | 4s / 480p | 4.04s | $0.3883 | $0.096114/s | $10/1M total tokens |

三条均为同一提示词的独立文生视频；分辨率和时长不同，不能当作同配置质量排名。美元/秒以实际解码时长折算。MiniMax与Kling没有传入未记录的关音频参数；实际音轨情况保留在evidence。NovaNova旧首帧任务仍单独待核对，本条Seedance2.5为不同输入的新案例。

![Cases](../screenshots/cn/video-models.png)

## kling-3.0-turbo

[![Preview](kling-3.0-turbo.jpg)](kling-3.0-turbo.mp4)

[Video](kling-3.0-turbo.mp4) · [Sanitized evidence](evidence/kling-3.0-turbo.json)

## MiniMax-H3

[![Preview](MiniMax-H3.jpg)](MiniMax-H3.mp4)

[Video](MiniMax-H3.mp4) · [Sanitized evidence](evidence/MiniMax-H3.json)

## seedance-2-5

[![Preview](seedance-2-5.jpg)](seedance-2-5.mp4)

[Video](seedance-2-5.mp4) · [Sanitized evidence](evidence/seedance-2-5.json)

## 运行方法

```powershell
python video_models.py --model MiniMax-H3 --prompt-file video-comparison/prompt.txt
python video_models.py --model MiniMax-H3 --prompt-file video-comparison/prompt.txt --live
```

不加--live只查同Key报价。支持这三个已检查档位，先保存提交记录，再轮询原任务，遇到不明确提交不自动重试。真实Key只放私有环境。

[MiniMax-H3](https://docs.toapis.com/docs/cn/api-reference/videos/minimax-h3/generation) · [Kling Turbo](https://docs.toapis.com/docs/cn/api-reference/videos/kling-3.0-turbo/generation) · [Seedance2.5](https://docs.toapis.com/docs/cn/api-reference/videos/seedance-2-5/generation)
