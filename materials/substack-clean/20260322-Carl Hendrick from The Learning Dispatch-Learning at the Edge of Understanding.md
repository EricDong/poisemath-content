---
title: "Learning at the Edge of Understanding"
date: 2026-03-22
source: Carl Hendrick, The Learning Dispatch
subtitle: "Correct answers are a lagging indicator of learning, not the mechanism."
---

# Learning at the Edge of Understanding

In 1929, the Knapp Electric Company sold a wooden box with two electrodes and a set of printed cards. The cards posed questions on topics from history to geography. You touched the electrodes to your answer; if you were right, the circuit closed and a light came on. If you were wrong, nothing happened. It was, in miniature, an assumption about learning that would prove extraordinarily durable: the idea that correctness is not merely the evidence that learning has occurred, but the very mechanism by which it happens.

[![](../substack/_assets/20260322-Carl%20Hendrick%20from%20The%20Learning%20Dispatch-Learning%20at%20the%20Edge%20of%20Understanding/https%253A%252F%252Fsubstack-post-media.s3.amazonaws.com%252Fpublic%252Fimages%252F05cc43b9-5895-4db7-bc93-8e22f14a67bf_799x546-db54d70ce7.jpeg)](https://substack.com/redirect/dac0973e-6cdd-43ff-bf52-9edfb390458e?j=eyJ1IjoiMXJ6YXV2In0.i_L8wvFkLUcXdz4pbEPfM8vw56XPotyGsyX7YQYkvWs)

Knapp Electric Questioner, c. 1929. Smithsonian National Museum of American History (CC0).

Three decades later, B.F. Skinner refined this intuition into something more sophisticated.  [He called it a teaching machine](https://substack.com/redirect/ce874b18-d692-4834-b1b2-cd16909d1842?j=eyJ1IjoiMXJ6YXV2In0.i_L8wvFkLUcXdz4pbEPfM8vw56XPotyGsyX7YQYkvWs) which advanced one small frame at a time, each requiring a correct response before the next would appear. But the premise was the same: arrange the material so that the student is almost always right, and learning will take care of itself. Again, correctness, in Skinner’s framework, *was* the learning. The reinforcement of right answers would shape behaviour, and shaped behaviour was all that mattered.

[![](../substack/_assets/20260322-Carl%20Hendrick%20from%20The%20Learning%20Dispatch-Learning%20at%20the%20Edge%20of%20Understanding/https%253A%252F%252Fsubstack-post-media.s3.amazonaws.com%252Fpublic%252Fimages%252F49166809-447f-42ef-9adc-62cf07df07e1_600x400-b186ebee13.jpeg)](https://substack.com/redirect/8e1c1c92-b8f9-4fef-8956-a65b3462d78c?j=eyJ1IjoiMXJ6YXV2In0.i_L8wvFkLUcXdz4pbEPfM8vw56XPotyGsyX7YQYkvWs)

Teaching machine designed by B.F. Skinner. National Museum of American History, Smithsonian Institution.

This idea still runs beneath a lot of adaptive learning software, many gamified apps, and AI tutoring systems that treat accuracy as both the measure and the engine of understanding. But a [recent study](https://substack.com/redirect/e2d65ebb-45ff-48df-8b83-68fd070ddd69?j=eyJ1IjoiMXJ6YXV2In0.i_L8wvFkLUcXdz4pbEPfM8vw56XPotyGsyX7YQYkvWs) suggests that this idea may have had the relationship exactly backwards. Correctness shows up *after* learning has already occurred. When learning is happening at the edge of understanding, correctness is often invisible.

### The Study: When Failure Became a Signal

[In the study,](https://substack.com/redirect/e2d65ebb-45ff-48df-8b83-68fd070ddd69?j=eyJ1IjoiMXJ6YXV2In0.i_L8wvFkLUcXdz4pbEPfM8vw56XPotyGsyX7YQYkvWs) the researchers took a language model and gave it a set of mathematical problems it could not solve. Not inconsistently, it failed completely. They then tried to improve its performance by training it directly on those problems. Nothing happened. The model was stuck: the problems were too hard to provide any useful signal, and without signal, there was no learning.

What came next was the interesting part. Rather than simplifying the problems or introducing easier ones, the researchers designed a framework in which the model generated its own intermediate tasks. These were not easier versions of the target problems, but structurally related ones that shifted in content and style as the learner improved: from word problems and basic formulas to concise, equation-heavy exercises in algebra and calculus.

Most of the answers to these problems were wrong. Accuracy remained low. And yet, learning restarted, and did so rapidly. Performance on the original hard problems began to improve, even though the model could not solve them at the outset and direct training on them alone had produced no progress.

[![](../substack/_assets/20260322-Carl%20Hendrick%20from%20The%20Learning%20Dispatch-Learning%20at%20the%20Edge%20of%20Understanding/https%253A%252F%252Fsubstack-post-media.s3.amazonaws.com%252Fpublic%252Fimages%252F9f328a4f-95c8-493e-a38b-45155791b56d_868x508-785129f002.png)](https://substack.com/redirect/44db02a3-7c73-4b30-911f-bba2f0979c18?j=eyJ1IjoiMXJ6YXV2In0.i_L8wvFkLUcXdz4pbEPfM8vw56XPotyGsyX7YQYkvWs)

Direct training on hard problems plateaus (red). Training on self-generated stepping-stone problems unlocks rapid improvement (pink). From Sundaram et al., 2026.

If correct answers were the mechanism of learning, this result would make little sense. What mattered was not success, but rather *exposure to structure.* The stepping-stone problems revealed something about the organisation of the domain: the kinds of relations that recurred, the representations that mattered, the transformations that preserved meaning. Even incorrect attempts reshaped the model’s internal representations in a productive direction. Correctness arrived later, as an outcome rather than a cause.

Perhaps the most interesting detail in the study is this: the “teacher” models that generated the intermediate problems were themselves largely wrong. Only 32.8% of their solutions were fully correct. And yet the “student” models still learned. As long as the problems were well-posed and conceptually relevant, they provided what the researchers call a “learnable gradient”: enough structure for the learner to gain traction. The accuracy of the answer mattered far less than the architecture of the question.

There is also a telling comparison buried in the results. A separate group of teachers, trained to optimise for a different signal, actually produced *more* correct answers: 55% accuracy. Yet their students learned *less*. Their questions collapsed into a narrow conceptual range, and in one case caused complete student failure. More correct answers, worse learning. The relationship between correctness and learning is not merely loose; under certain conditions, it inverts entirely.

This is a finding that I think is really interesting for instructional design because it suggests that learning happens not by mimicking a perfect answer, but by engaging with the right conceptual structure. A well-constructed problem, even one accompanied by a flawed solution, can open up a region of understanding that a correct but poorly structured exercise never touches. Structure beats accuracy. In other words, the map matters more than the destination marker.

---

### The Productive Failure Problem

This also helps clarify a persistent confusion in education around the idea of [productive failure](https://substack.com/redirect/af4f31bd-bbc5-4854-b324-c82aa9e042c9?j=eyJ1IjoiMXJ6YXV2In0.i_L8wvFkLUcXdz4pbEPfM8vw56XPotyGsyX7YQYkvWs). Repeated failure on the original hard problems produced no learning signal at all. It was only once the learner encountered problems that were, in some meaningful sense, learnable that failure became informative. Learning did not arise from struggle per se, but from struggle within a structure that could be partially apprehended. Struggle without structure is not a [desirable difficulty](https://substack.com/redirect/380fb423-3f56-44bd-9cd0-fb0359d46b14?j=eyJ1IjoiMXJ6YXV2In0.i_L8wvFkLUcXdz4pbEPfM8vw56XPotyGsyX7YQYkvWs). It is simply noise.

This distinction matters because the debate around productive failure has often been poorly drawn. As [Greg Ashman](https://open.substack.com/users/12430510-greg-ashman?utm_source=mentions) has [argued](https://substack.com/redirect/a03c33b4-4a15-480f-b6ad-d28999308027?j=eyJ1IjoiMXJ6YXV2In0.i_L8wvFkLUcXdz4pbEPfM8vw56XPotyGsyX7YQYkvWs), the research base for productive failure is weaker than its advocates suggest, and the ethical implications of intentionally causing students to struggle are rarely examined. He is right on both counts. Intentionally designing lessons around failure, without specifying the conditions under which that failure becomes informative, is not a pedagogy; it is an abdication. The students most likely to flounder are precisely those who are already least advantaged: the ones who bring the fewest resources to a problem and stand to lose the most from another experience of not knowing. As Ashman puts it, intentionally causing struggle and then mitigating the negative effects is “like intentionally making a hole in the bottom of a row boat and then grabbing a bucket to bail out the water.”

### At the Edge of Learnability

The study reinforces this concern: unstructured failure on problems beyond the learner’s reach produced nothing at all. But it also reveals something the productive failure debate has largely missed. What restarted learning was not success, nor explicit instruction, nor even easier problems. It was problems with the right internal structure: problems that made the organisation of the domain partially visible, even when the learner could not yet solve them. The question is not whether students should struggle. It is whether the task they are given has enough conceptual architecture to make that struggle legible.

Seen this way, [the concept of scaffolding](https://substack.com/redirect/bec00dfa-8295-4e67-9818-9f7f4e1dc1f6?j=eyJ1IjoiMXJ6YXV2In0.i_L8wvFkLUcXdz4pbEPfM8vw56XPotyGsyX7YQYkvWs) also sharpens. Scaffolding is often misunderstood as making tasks easier, or as providing hints, encouragement, or additional support. But none of these capture its essential function. A scaffold is not a ramp; it is a lens. It changes what the learner can see and work with. It makes the structure of the domain visible and usable, altering what the learner can do later, not how well they perform now.

The paper also exposes a limitation in many AI tutoring systems, and in more than a few classrooms. These systems adapt to performance indicators: correctness, speed, confidence etc. Yet at the edge of learnability, these signals are largely meaningless. Learning is either beginning or failing to begin long before performance becomes stable or interpretable. A system that optimises for immediate accuracy at the frontier of a student’s understanding is like a gardener who judges growth by pulling up the seedling to check the roots.

A genuinely intelligent tutoring system would not optimise for immediate success. It would optimise for learning trajectories: the slow, often invisible reshaping of representation that precedes competence. It would tolerate incorrect answers when they indicate progress in understanding, and it would judge instruction by delayed transfer rather than local accuracy. The 32.8% figure from this study is a provocation: it implies that the quality of the question a system poses may matter more than whether it can supply the correct answer.

### What Correctness Cannot Tell Us

For teachers, the lesson is familiar, but still worth stating plainly. Good instruction does not aim to maximise success in the moment. It aims to make success possible *later*. As [Dylan Wiliam](https://open.substack.com/users/18561168-dylan-wiliam?utm_source=mentions) notes, the purpose of feedback is to improve the student and not the work.

[Rosenshine](https://substack.com/redirect/df9ee2ba-da6c-48ac-a345-4275539693d9?j=eyJ1IjoiMXJ6YXV2In0.i_L8wvFkLUcXdz4pbEPfM8vw56XPotyGsyX7YQYkvWs) was right that effective teachers obtain a high success rate, but the art lies in understanding what makes that success rate possible: not the avoidance of difficulty, but the careful construction of tasks whose structure a learner can get hold of. The right problem, at the right time, with enough architecture to make the struggle productive.

I have [written before](https://substack.com/redirect/6682a719-0904-494e-ae9f-9b32c060de03?j=eyJ1IjoiMXJ6YXV2In0.i_L8wvFkLUcXdz4pbEPfM8vw56XPotyGsyX7YQYkvWs) about what happens when correct answers arrive without learning: watching my daughter completing a phonics puzzle by matching colours, producing perfect scores while the cognitive architecture beneath remained untouched. This study reveals the inverse: what happens when learning arrives without correct answers. Together, they suggest that correctness and learning are far more loosely coupled than our systems assume. Correct answers tell us what learning has already achieved. They tell us very little about how to bring it about.

Skinner's teaching machine was an intricate piece of engineering in service of a half-truth. Correctness is not irrelevant; it is the destination. But it is not the mechanism. In 1929, the Knapp Electric Questioner offered a closed circuit for the right answer and silence for the wrong one. Nearly a century later, most of our educational technology still operates on the same principle. The SOAR study suggests we have been listening for the wrong signal. Learning does not announce itself with a light. It begins in the silence, in the space where the circuit has not yet closed but the structure of the problem is slowly becoming visible.

---

[![](../substack/_assets/20260322-Carl%20Hendrick%20from%20The%20Learning%20Dispatch-Learning%20at%20the%20Edge%20of%20Understanding/https%253A%252F%252Fsubstack.com%252Ficon%252FLucideCheck%253Fv%253D4%2526height%253D40%2526fill%253Dtransparent%2526stroke%253D%252523FF6719%2526stro-3bff44912e.6)Subscribed](https://carlhendrick.substack.com/account.MmgoPdJs3scb0wSFdfNFCvTOZGlhz2dwqf___Fzo2u4?)
