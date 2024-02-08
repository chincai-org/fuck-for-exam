<script lang="ts">
    import { getQuestion } from "$lib/data/fetchData";
    import type { Question } from "$lib/data/types";

    export let questions: Array<string | any>;
    export let next: (score: number) => void;

    console.log(questions);

    let wrongs: Array<Question> = [];

    let current = 0;
    let correctAmount = 0;
    let question: Question;
    let askWrong = false;
    let answered = false;
    let correct = false;
    let lastChoice: string;
    $: {
        question = getQuestion(askWrong ? wrongs[current].id : questions[current]) as Question;
        console.log(current, askWrong, question);
    }
    $: choices = question.shuffle
        ? question.choices.toSorted(() => Math.random() - 0.5)
        : question.choices;

    function validate(choice: string) {
        if (!askWrong) {
            if (choice == question.answer) {
                correct = true;
                correctAmount++;
            } else {
                correct = false;
                wrongs.push(question);
            }
        } else {
            if (choice != question.answer) {
                correct = false;
                wrongs.push(question);
            } else {
                correct = true;
            }

            wrongs.shift();
        }
    }

    function clickChoice(choice: string) {
        return (_: any) => {
            if (answered) return;

            validate(choice);
            lastChoice = choice;
            answered = true;
        };
    }

    function nextQuestion() {
        if (!askWrong) {
            // Answering normal questions
            if (current == questions.length - 1) {
                // No more questions left

                // Check if have wrong questions
                if (wrongs.length > 0) {
                    // If got wrong
                    current = 0;
                    askWrong = true;
                } else {
                    // No wrong, go to next level
                    next(correctAmount / questions.length);
                }
            } else {
                // Got questions left, go to next question
                current++;
            }
        } else {
            // Answering wrong questions
            if (wrongs.length == 0) {
                // No wrong questions left
                next(correctAmount / questions.length); // go to next level
            }

            // Shuffle the wrong question list (apparantly this is the best solution I figured out to trigger the reactivity event)
            wrongs = wrongs.toSorted(() => Math.random() - 0.5);
        }

        // Remove the result
        answered = false;
    }
</script>

{#if askWrong}
    Previous mistake
{/if}

{#if question.questionType == "vocab"}
    <p>What is the definition of the following word?</p>
{/if}

<p>{question.question}</p>

{#if question.answerType == "objective"}
    {#each choices as choice}
        {#if answered}
            {#if choice == question.answer}
                <button
                    class="--button correct"
                    data-button="question"
                    on:click={clickChoice(choice)}>{choice}</button
                >
            {:else if choice == lastChoice}
                <button class="--button wrong" data-button="question" on:click={clickChoice(choice)}
                    >{choice}</button
                >
            {:else}
                <button class="--button" data-button="question" on:click={clickChoice(choice)}
                    >{choice}</button
                >
            {/if}
        {:else}
            <button class="--button" data-button="question" on:click={clickChoice(choice)}
                >{choice}</button
            >
        {/if}
    {/each}
{/if}

{#if answered}
    <div>
        <p>{correct ? "Correct" : "Wrong"}</p>
        {#if !correct}
            <p>Correct: {question.answer}</p>
        {/if}
        <button class="--button" data-button="accent" on:click={nextQuestion}>Continue</button>
    </div>
{/if}

<style lang="scss">
    @use "/src/lib/sass/abstracts/" as *;

    [data-button="question"] {
        background-color: $button-accent-background;
        color: $button-accent-color;

        &:is(:hover, :focus) {
            background-color: $button-accent-background-hover;
            color: $button-accent-color-hover;
        }
    }

    .correct {
        background-color: $color-primary-green-500;

        &:is(:hover, :focus) {
            background-color: $color-primary-green-600;
            color: black;
        }
    }

    .wrong {
        background-color: $color-primary-red-500;

        &:is(:hover, :focus) {
            background-color: $color-primary-red-600;
            color: black;
        }
    }
</style>
