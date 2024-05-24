/*
 * Copyright 2002-2024 the original author or authors.
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *      https://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */

package org.springframework.test.json;

import org.springframework.http.converter.GenericHttpMessageConverter;
import org.springframework.lang.Nullable;

/**
 * Default {@link AbstractJsonContentAssert} implementation.
 *
 * @author Stephane Nicoll
 * @since 6.2
 */
public class JsonContentAssert extends AbstractJsonContentAssert<JsonContentAssert> {

	/**
	 * Create an assert for the given JSON document.
	 * <p>Path can be converted to a value object using the given
	 * {@linkplain GenericHttpMessageConverter JSON message converter}.
	 * @param json the JSON document to assert
	 * @param jsonMessageConverter the converter to use
	 */
	public JsonContentAssert(@Nullable String json, @Nullable GenericHttpMessageConverter<Object> jsonMessageConverter) {
		super(json, jsonMessageConverter, JsonContentAssert.class);
	}

}
