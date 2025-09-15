---
title: "GSoC 2025 Project summary. BuffaLogs: Alerting Module Enhancement"
authors: ["Kunal Gurtatta"]
date: "2025-09-15T11:00:06+01:00"
tags: ["gsoc", "buffalogs"]
---

**Contributor**: Kunal Gurtatta
**Mentors:** Lorena Goldoni, Federico Foschini

## Overview
As a Python developer and security enthusiast, I always wanted to contribute to open-source security projects. When I learned about GSoC from one of my seniors, I started searching for security organizations and came across Honeynet. They had just announced their ideas for this year's GSoC, and one of them was BuffaLogs, which matched my tech stack perfectly. I began contributing in late Feb'25, submitting PRs to implement alerters and making small refactors to get familiar with the codebase. Since my early contributions focused on alerters, I decided to continue working on integrating more of them and improving the alerting logic in my proposal.
<!--more-->
## Pre-GSOC Commits/Discussions

- [#129](https://github.com/certego/BuffaLogs/pull/129) (**Merged**) Added Email Alert Functionality
- [#141](https://github.com/certego/BuffaLogs/pull/141) (**Merged**) Added Pushover Alerter Functionality
- [#181](https://github.com/certego/BuffaLogs/pull/187) (**Merged**) Added Discord Alerter
- [#190](https://github.com/certego/BuffaLogs/pull/190) (**Merged**) Moved Slack Alerter Import to Top
- [#196](https://github.com/certego/BuffaLogs/pull/196) (**Merged**) Refactored Hardcoded Paths
- [#223](https://github.com/certego/BuffaLogs/pull/223) (**Merged**) Refactor run.sh
- [#225](https://github.com/certego/BuffaLogs/pull/225) (**Merged**) Refactor tasks.py to handle code duplication
- [#171](https://github.com/certego/BuffaLogs/issues/171) (**Discussion**) Enhancement: Add Support for Multi-Factor Authentication (MFA) Monitoring

## GSoC Deliverables

#### <u>P1 New Alerting Sources</u>
Three new alerters were added to BuffaLogs:
- RocketChat: [#291](https://github.com/certego/BuffaLogs/pull/291)
- Mattermost: [#298](https://github.com/certego/BuffaLogs/pull/298)
- GoogleChat: [#289](https://github.com/certego/BuffaLogs/pull/289)

#### <u>P1 Standardization of Alerting Module</u> [#303](https://github.com/certego/BuffaLogs/pull/303)
I refactored and standardized all the alerting modules, ensuring that all alerters and their respective tests have a similar structure. This improved maintainability and made it easier to add new alerting sources. The structure of the alerters was further updated in future PRs as new features were implemented.

#### <u>P1 Comprehensive Testing</u> [#309](https://github.com/certego/BuffaLogs/pull/309)
I improved the test setup and added new tests to cover edge cases, such as:
- `test_no_alerts`: Ensures no alerts are sent when there are none to notify.
- `test_improper_config`: Checks that an error is raised if the configuration is incorrect.
- `test_alert_network_failure`: Verifies that an alert is not marked as notified if there are network failures.
Later, another test was added for clubbed alerts. All alerters now follow the same structure for tests.

#### <u>P1 Alert Message Formatter</u> [#315](https://github.com/certego/BuffaLogs/pull/315)
This task was a precursor to `P2 Customizable templates`. I added `alert_message_formatter` to the `BaseAlerting` class, which takes an alert as an argument and returns the title and description. No Jinja templates were used here; instead, hardcoded text was used in the formatter. While not ideal, it was still an improvement over the previous implementation.

#### <u>P2 Email Integration in Users Model</u> [#320](https://github.com/certego/BuffaLogs/pull/320)
Initially, the idea was to add a new `email` field to the `Users` model to notify users via email if there was an alert for them. However, after discussions, we decided to create a mapping in the config itself, since logs are external and may not contain such a field. Separate mappings `recipient_list_admins` and `recipient_list_users` were created in `config/alerting.json`, allowing organizations to easily map their users to their respective emails. 
A new Jinja template, `alert_template_user_email.jinja`, was also added for notifying users with a different alert message.

#### <u>P2 Alert Preferences System</u> [#322](https://github.com/certego/BuffaLogs/pull/322)
This was a feature I personally wanted when I started contributing to BuffaLogs. Previously, only one alerting source could be implemented, which wasn't practical. Organizations often need multiple notification sources working simultaneously with different priorities. After discussions with Lorena and Federico, we decided to update the `notified` field of alerts to `notified_status`, tracking each alerter's notification status. 
This required a major revamp of `alert_factory`, which taught me a lot. `NotifyAlertsTask` was also updated to support the new feature. I wrote a comprehensive test, `test_alert_factory`, to cover every edge case I could think of, ensuring no alert gets missed ;)

#### <u>P2 Retry Mechanism with Exponential Backoff</u> [#348](https://github.com/certego/BuffaLogs/pull/348)
I initially implemented a custom logic for exponential backoff when sending messages failed due to network issues, not realizing a library already existed for this. Federico suggested using the `backoff` decorator, which worked perfectly and simplified the code. I separated the request logic into a new function, `send_message`, which handles the requests for sending notifications.

#### <u>P2 Customizable Templates</u> [#350](https://github.com/certego/BuffaLogs/pull/350)
This was a particularly interesting and time saving task. Until now, alert titles and descriptions were hardcoded in each alerter, making it difficult to change messages and reducing uniformity (even the `Alert Message Formatter` wasn't enough). With help from my mentors, I implemented two Jinja templates `alert_template.jinja` and `alert_template_user_email.jinja`. 
Now, we can simply pass the alert as an argument and get the title and description, making it easy to customize alert messages as needed. During this task, I learned a lot about Jinja templates, including how to create them, pass arguments, and render content. The `alert_message_formatter` was also refactored to use these templates.

#### <u>P3 Slack Integration Enhancements</u> [#372](https://github.com/certego/BuffaLogs/pull/372)
For platform specific enhancements Slack was chosen, tagging of affected users and thread based conversations were proposed but when I started working on it I realised that for thread based conversations Slack API needs to be used, webhooks were not enough for that. So, we decided to stick with the tagging of affected users only. Similar to email, here also mapping of users with their slack usernames wass done in the config.

#### <u>Remove `test_send_actual_alert` from alerter tests</u> [#378](https://github.com/certego/BuffaLogs/pull/378)
Due to the backoff mechanism real alerts which would fail in a test environment started pilling up,increasing the test duration leading to failures. Hence they were completely removed from all the alerter tests.

#### <u>P3 Configurable Thresholds, Aggregation Options, and Rate Limiting for Alerts (Merged)</u> [#402](https://github.com/certego/BuffaLogs/pull/402)
This task required a lot of thought and discussion, as the objectives overlapped, so a single PR was made. The main goal was to club similar alerts within a given window based on user, to avoid flooding with multiple alerts in a short interval (e.g. a brute-force attempt). 
A new Jinja template for clubbed alerts was created. The `alert_message_formatter` was refactored to accept any number of arguments depending on the use case. Alerts are now filtered based on a specified range to group them if the gap is less than the desired range (30 min). Single alerts are notified as before, while clubbed alerts use a separate template. 
The `NotifyAlertsTask` was updated to support this new range. A new test, `test_clubbed_alerts`, was written (and later improved) to check if clubbing works correctly.

#### <u>P4 Scheduled Digests</u> [#419](https://github.com/certego/BuffaLogs/pull/419)
The enormous Scheduled Digests PR required refactoring almost everything from the ground up! All alerters were improved, separating the logic for sending requests, sending summaries, and managing notifications. 
A new task, `ScheduledAlertSummaryTask`, was created to run daily or weekly, depending on user choice. Its job? Sending simple alert summaries of everything that happened during that period, giving users a brief overview. 
Writing `test_tasks` was unexpectedly time-consuming, as I had to figure out how to create alerts with different creation dates and ensure only those in the specified range were included in the summary. For future contributors, here's a tip: 
```
alert1 = Alert.objects.create(
    user=self.user1,
    name="Imp Travel",
    login_raw_data={},
    # having the created field in the alert itself
    created=start_date + timedelta(hours=1)
)
```
This didn't work as expected, so I did this instead:
```
Alert.objects.filter(id=alert1.id).update(created=start_date + timedelta(hours=1))
alert1.refresh_from_db()
```
And it worked! (Don't ask me how or why.)

#### <u>P4 Documentation</u> [#408](https://github.com/certego/BuffaLogs/pull/408)
This was a fairly simple task, documenting how alerters work, how to set them up, and how to create your own. More documentation may be added in the future as needed.

## Ending Note and Post-GSoC
GSoC has been a rewarding and educational journey for me. I learned a lot about open source, which once felt intimidating. I gained experience working in a collaborative environment, writing good tests (very important!), and thinking creatively. 
I want to thank Lorena and Federico, my mentors, who were always there to help whenever I was stuck. It was great connecting with them and having insightful discussions. 
In the future, I plan to explore more of the open-source world and keep contributing to BuffaLogs whenever I can. It feels good to give back to the community that helped me learn so much.