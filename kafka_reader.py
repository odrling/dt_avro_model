import faust

app = faust.App("kafka-reader")
topic = app.topic('my_topic3')


@app.agent(topic)
async def reader(events):
    async for event in events:
        print(event)


if __name__ == '__main__':
    app.main()
