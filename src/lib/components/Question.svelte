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
    let btns = {}
    $: {
        question = getQuestion(askWrong ? wrongs[current].id : questions[current]) as Question;
        console.log(current, askWrong, question);
    }
    $: choices = question.shuffle
        ? question.choices.toSorted(() => Math.random() - 0.5)
        : question.choices;

    $: choices.forEach((element) => {
        btns[element] = "--button --bg-accent-400";
    });

    $: console.log(btns)

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
        btns[choice] == ""
        return (_: any) => {
            validate(choice);
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
    {#each Object.keys(btns) as btn}
        <button class={btns[btn]} on:click={clickChoice(btn)}>{btn}</button>
    {/each}
{/if}

{#if answered}
    <div>
        <p>{correct ? "Correct" : "Wrong"}</p>
        {#if !correct}
            <p>Correct: {question.answer}</p>
        {/if}
        <button on:click={nextQuestion}>Next question</button>
    </div>
{/if}

<style lang="scss">
    @use "/src/lib/sass/abstracts/" as *;


    .correct {
        background-color: $color-green-600;
    }

    .wrong {
        background-color: $color-red-600;
    }
</style>
