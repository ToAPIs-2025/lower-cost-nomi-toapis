# More video models: same-prompt T2V cases and charges

2026-10-20.

| Model | Request | Decoded length | API-settled cost | Case USD/s | Current preset rate |
|---|---|---:|---:|---:|---|
| kling-3.0-turbo | 4s / 720p | 4.04s | $0.32 | $0.079208/s | $0.08/s |
| MiniMax-H3 | 5s / 768p | 5.17s | $0.32 | $0.061896/s | $0.064/s |
| seedance-2-5 | 4s / 480p | 4.04s | $0.3883 | $0.096114/s | $10/1M total tokens |

All three are independent text-to-video calls using the same prompt. Resolution and duration differ, so this is not a matched-settings quality ranking. USD/s divides the settled charge by decoded duration. Audio-track observations are in evidence; no undocumented audio switch was supplied to MiniMax or Kling. This new Seedance 2.5 case does not resolve the separate uncertain NovaNova I2V submission.

![Cases](../screenshots/en/video-models.png)

## kling-3.0-turbo

[![Preview](kling-3.0-turbo.jpg)](kling-3.0-turbo.mp4)

[Video](kling-3.0-turbo.mp4) · [Sanitized evidence](evidence/kling-3.0-turbo.json)

## MiniMax-H3

[![Preview](MiniMax-H3.jpg)](MiniMax-H3.mp4)

[Video](MiniMax-H3.mp4) · [Sanitized evidence](evidence/MiniMax-H3.json)

## seedance-2-5

[![Preview](seedance-2-5.jpg)](seedance-2-5.mp4)

[Video](seedance-2-5.mp4) · [Sanitized evidence](evidence/seedance-2-5.json)

## Run

```powershell
python video_models.py --model MiniMax-H3 --prompt-file video-comparison/prompt.txt
python video_models.py --model MiniMax-H3 --prompt-file video-comparison/prompt.txt --live
```

Without --live, query the current-key rate only. The client enables only the inspected presets, persists before submission and resumes existing tasks. Uncertain submissions are not retried. Keep the generation key private.

[MiniMax-H3](https://docs.toapis.com/docs/cn/api-reference/videos/minimax-h3/generation) · [Kling Turbo](https://docs.toapis.com/docs/cn/api-reference/videos/kling-3.0-turbo/generation) · [Seedance2.5](https://docs.toapis.com/docs/cn/api-reference/videos/seedance-2-5/generation)
