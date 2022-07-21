package com.dodam.mapper;

import java.io.IOException;

import org.apache.hadoop.io.IntWritable;
import org.apache.hadoop.io.LongWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Mapper;

import com.dodam.common.AirlinePerformanceParser;
import com.dodam.common.DelayCounters;

public class DelayCountMapperWithAirportOption extends Mapper<LongWritable, Text, Text, IntWritable> {
	private String workType;
	private final static IntWritable outputValue = new IntWritable(1);
	private Text outputKey = new Text();

	// 최초 맵 생성될대 한번 실행되는(초기화 되는 메서드)
	@Override
	protected void setup(Mapper<LongWritable, Text, Text, IntWritable>.Context context)
			throws IOException, InterruptedException {
		// TODO Auto-generated method stub
		workType = context.getConfiguration().get("workType");
	}

	@Override
	protected void map(LongWritable key, Text value, Mapper<LongWritable, Text, Text, IntWritable>.Context context)
			throws IOException, InterruptedException {
		// TODO Auto-generated method stub
		AirlinePerformanceParser parser = new AirlinePerformanceParser(value);
		outputKey.set(parser.getYear() + "," + parser.getMonth());
		// -D workType=[D,A]-[JFK]
		// -D workType=D-999 --> 다 뽑아라
		if (workType.split("-")[0].equals("departure")) {
			// if user input = 999
			if (parser.isDepartureDelayAvailable()) {
				if (workType.split("-")[1].equals("999")) {
					if (parser.getDepartureDelayTime() > 0) {
						context.write(outputKey, outputValue);
					} else if (parser.getDepartureDelayTime() == 0) {
						context.getCounter(DelayCounters.scheduled_departure).increment(1);
					} else if (parser.getDepartureDelayTime() < 0) {
						context.getCounter(DelayCounters.early_departure).increment(1);
					}
				} else {
					// if user input has airport name
					String airport = workType.split("-")[1];
					if (parser.getOrigin().equals(airport)) {
						if (parser.isDepartureDelayAvailable()) {
							if (parser.getDepartureDelayTime() > 0) {
								context.write(outputKey, outputValue);
							} else if (parser.getDepartureDelayTime() == 0) {
								context.getCounter(DelayCounters.scheduled_departure).increment(1);
							} else if (parser.getDepartureDelayTime() < 0) {
								context.getCounter(DelayCounters.early_departure).increment(1);
							}
						}
					}
				}
			} else {
				context.getCounter(DelayCounters.not_available_departure).increment(1);
			}

		} else if (workType.split("-")[0].equals("arrival")) {
			if (parser.isArrivalDelayAvailable()) {
				if (workType.split("-")[1].equals("999")) {
					if (parser.getArrivalDelayTime() > 0) {
						context.write(outputKey, outputValue);
					} else if (parser.getArrivalDelayTime() == 0) {
						context.getCounter(DelayCounters.scheduled_arrival).increment(1);
					} else if (parser.getArrivalDelayTime() < 0) {
						context.getCounter(DelayCounters.early_arrival).increment(1);
					}
				} else {
					// if user input has airport name
					String airport = workType.split("-")[1];
					if (parser.getDestination().equals(airport)) {
						if (parser.getArrivalDelayTime() > 0) {
							context.write(outputKey, outputValue);
						} else if (parser.getArrivalDelayTime() == 0) {
							context.getCounter(DelayCounters.scheduled_arrival).increment(1);
						} else if (parser.getArrivalDelayTime() < 0) {
							context.getCounter(DelayCounters.early_arrival).increment(1);
						}
					}
				}
			} else {
				context.getCounter(DelayCounters.not_available_arrival).increment(1);
			}
		}
	}
}
